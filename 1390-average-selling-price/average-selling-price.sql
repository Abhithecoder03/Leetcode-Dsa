# Write your MySQL query statement below
select Prices.product_id ,IFNULL(round(sum(price*units)/sum(units),2),0) as average_price from Prices
left join UnitsSold on  UnitsSold.product_id=Prices.product_id
and purchase_date BETWEEN start_date AND end_date 
group by Prices.product_id