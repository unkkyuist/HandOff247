using System.ComponentModel;
using ModelContextProtocol.Server;
namespace Mini;

[McpServerToolType]
public sealed class McpTools(Operations operations)
{
    Task<object> Call(string op, params string[] args) => operations.Execute(op, args);
    [McpServerTool, Description("List records. Returns [{id}] items.")]
    public Task<object> List() => Call("list");
    [McpServerTool, Description("Add a note to a record.")]
    public Task<object> AddNoteAsync(string text) => Call("notes.add", text);
    [McpServerTool(Name = "record_get"), Description("Read one record.")]
    public Task<object> Get(string id) => Call("get", id);
}
