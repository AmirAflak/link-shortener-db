CREATE PROCEDURE get_url
    @short_url CHAR(6),
    @original_url VARCHAR(255) OUTPUT
AS
BEGIN
    -- Check if short URL exists and retrieve original URL
    SELECT @original_url = original_url
    FROM urls
    WHERE short_url = @short_url

    -- Raise error if short URL does not exist
    IF @original_url IS NULL
    BEGIN
        RAISERROR('Short URL not found', 16, 1)
        RETURN
    END
END