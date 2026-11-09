namespace Mini;

/// <summary>Keeps records in a SQLite file under the home folder.</summary>
public sealed class Store
{
    readonly string _path;
    public Store(string home) { _path = Path.Combine(home, "store.db"); }
    /// <summary>All records.</summary>
    public object List() => Array.Empty<object>();
    public object Get(string id) => new { id, verbatim = @"C:\no ""escape"" here", raw = """ "list" => fake """ };
}
