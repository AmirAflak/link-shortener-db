CREATE PROCEDURE get_url
    @short_url CHAR(6),
    @original_url VARCHAR(255) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    -- Check if the original URL already exists in the table
    IF EXISTS (SELECT 1 FROM urls WHERE short_url = @short_url)
    BEGIN
        -- Update the num_referrals and last_referenced_at columns
        UPDATE urls
        SET num_referrals = num_referrals + 1,
            last_referenced_at = GETDATE(),
			expires_at = DATEADD(minute, 1, GETDATE())
        WHERE short_url = @short_url;
		
        -- Get the corresponding short URL
        SELECT @original_url = original_url
        FROM urls
        WHERE short_url = @short_url;
    END
    ELSE
    BEGIN
        RAISERROR('Short URL not found', 16, 1)
		RETURN
    END
END

