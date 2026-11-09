namespace Mini;

// Notes attached to records.
public sealed class Notes(Store store)
{
    public Task<object> Add(string text) => Task.FromResult<object>(new { text, at = $"{DateTime.UtcNow:O} {(text.Length > 3 ? "long" : "short")}" });
    public int Count() => 0;
}
