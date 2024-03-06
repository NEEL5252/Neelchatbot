-- Replace 'your_table_name' with the name of your table
-- Replace 'new_starting_id' with the new starting ID you want (in this case, 1)
BEGIN TRANSACTION;
UPDATE sqlite_sequence SET seq='new_starting_id' WHERE name='chatbox_new_order';
UPDATE chatbox_new_order SET id = id - (SELECT MIN(id) FROM chatbox_new_order) + 1;
COMMIT;
-- 