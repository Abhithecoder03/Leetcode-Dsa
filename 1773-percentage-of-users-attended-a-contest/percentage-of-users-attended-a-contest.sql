# Write your MySQL query statement below
select Register.contest_id,ROUND(count(Register.user_id) * 100/(
    SELECT COUNT(user_id) from Users 
), 2) as percentage from Register
left join Users on Users.user_id=Register.user_id
group by contest_id
ORDER BY percentage DESC, contest_id ASC