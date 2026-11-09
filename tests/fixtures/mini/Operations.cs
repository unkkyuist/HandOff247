namespace Mini;

/// <summary>Single entry point for every operation the app supports.</summary>
public sealed class Operations(Store store)
{
    public async Task<object> Execute(string operation, string[] args)
    {
        var notes = new Notes(store);
        var label = "not \"a\" => key"; // a string that looks like an arm must be ignored
        return operation switch
        {
            "list" => store.List(),
            "get" => store.Get(args[0]),
            "notes.add" => await notes.Add(args[0]),
            "notes.count" or "notes.size" => notes.Count(),
            "info" => new { name = "mini", label },
            _ => throw new InvalidOperationException("unknown")
        };
    }
}
