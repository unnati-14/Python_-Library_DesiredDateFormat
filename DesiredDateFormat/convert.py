def convert(date, format):
    date=str(date)[:10]
    separator = '-'
    if '/' in date:
        separator = '/'
    if(format=="mm/dd/yy"):        
        res = convert_to_month_date_year(date, separator)
    elif(format=="dd/mm/yy"):
        res = convert_to_date_month_year(date, separator)
    elif(format=="yy/mm/dd"):
        res = convert_to_year_month_date(date, separator)
    else:
        return "please provide valid format [mm/dd/yy or dd/mm/yy or yy/mm/dd]"
    return res

def convert_to_month_date_year(date, separator):
    l = date.split(separator)
    new_date = l[1]+separator+l[2]+separator+l[0]
    return new_date

def convert_to_date_month_year(date, separator):    
    l = date.split(separator)
    new_date = l[2]+separator+l[1]+separator+l[0]
    return new_date

def convert_to_year_month_date(date, separator):    
    l = date.split(separator)
    new_date = l[0]+separator+l[1]+separator+l[2]
    return new_date
