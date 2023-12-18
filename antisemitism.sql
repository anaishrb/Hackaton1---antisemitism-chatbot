-- Create a table to store text data
--CREATE TABLE text_data (
--    id SERIAL PRIMARY KEY,
--    text_content TEXT,
--    label INTEGER
--);
-- Insert sample data into the table
INSERT INTO text_data (text_content, label) VALUES 
    ('Jews are bad', 1),  -- Example of hate speech
    ('I admire the Jewish culture', 0),  -- Non-hateful content
    ('Jews are not good people', 1),  -- Additional hate speech
    ('To be Jews is a religion and not a definer of someone being a bad or good people, as any other religion', 0);  -- Corresponding non-hateful content
