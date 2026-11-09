// Mini app used by the HandOff247 tests: one binary, three modes, one dispatch table.
using Mini;

var home = Environment.GetEnvironmentVariable("APP_HOME") ?? "data";
var store = new Store(home);
var operations = new Operations(store);
var mode = args.FirstOrDefault() ?? "serve";
if (mode == "cli")
{
    var op = args.ElementAtOrDefault(1) ?? "list";
    Console.WriteLine(await operations.Execute(op, args.Skip(2).ToArray()));
    return;
}
if (mode == "mcp")
{
    var builder = Host.CreateApplicationBuilder();
    builder.Services.AddMcpServer().WithStdioServerTransport().WithTools<McpTools>();
    await builder.Build().RunAsync(); return;
}
if (mode is not ("serve" or "server")) { Console.Error.WriteLine("usage"); return; }

var web = WebApplication.CreateBuilder();
var port = Environment.GetEnvironmentVariable("APP_PORT") ?? "5050";
web.WebHost.UseUrls($"http://127.0.0.1:{port}");
var app = web.Build();
app.MapPost("/api/{operation}", async (string operation) => await operations.Execute(operation, []));
app.MapGet("/health", () => "ok");
app.UseStaticFiles();
var path = Path.Combine(home, "mini.db");
await app.RunAsync();
