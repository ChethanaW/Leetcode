# Write your MySQL query statement below


SELECT id,
    MAX(if(month = 'Jan',revenue, null )) AS Jan_Revenue,
    MAX(if(month = 'Feb',revenue, null )) AS Feb_Revenue,
    MAX(if(month = 'Mar',revenue, null )) AS Mar_Revenue,
    MAX(if(month = 'Apr',revenue, null )) AS Apr_Revenue,
    MAX(if(month = 'May',revenue, null )) AS May_Revenue,
    MAX(if(month = 'Jun',revenue, null )) AS Jun_Revenue,
    MAX(if(month = 'Jul',revenue, null )) AS Jul_Revenue,
    MAX(if(month = 'Aug',revenue, null )) AS Aug_Revenue,
    MAX(if(month = 'Sep',revenue, null )) AS Sep_Revenue,
    MAX(if(month = 'Oct',revenue, null )) AS Oct_Revenue,
    MAX(if(month = 'Nov',revenue, null )) AS Nov_Revenue,
    MAX(if(month = 'Dec',revenue, null )) AS Dec_Revenue
FROM Department
GROUP BY id;