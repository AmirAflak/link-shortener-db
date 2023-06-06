CREATE FUNCTION get_url(@short_url CHAR(6))
RETURNS VARCHAR(255)
AS
BEGIN
    DECLARE @original_url VARCHAR(255)

    -- Check if short URL exists and retrieve original URL
    SELECT @original_url = original_url
    FROM urls
    WHERE short_url = @short_url

    -- Raise error if short URL does not exist
    IF @original_url IS NULL
    BEGIN
        THROW 50001, 'Short URL not found', 1
    END

    RETURN @original_url
END