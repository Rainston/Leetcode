# Write your MySQL query statement below
SELECT distinct viewer_id AS id from Views where author_id = viewer_id order by id;