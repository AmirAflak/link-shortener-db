DECLARE @result VARCHAR(255)
EXEC get_url 'abc123', @result OUTPUT
SELECT @result