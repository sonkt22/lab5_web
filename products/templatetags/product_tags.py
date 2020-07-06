from django import template

register = template.Library()

@register.filter(name='cut_description')
def cut_description(value, arg):
    temp = value.split(" ")
    res = ""
    for i in range(arg):
        if i < len(temp):
            res += temp[i] + " "
        else:
            break
    return res

@register.filter(name='add_point')
def add_point(value):
    res = '' #1000
    temp = value
    i = 0
    while temp != 0:
        str_value = str(temp)
        res = str_value[len(str_value)-1] + res
        temp = temp//10
        i+=1
        if i == 3 and temp!=0:
            res = '.'+res
            i=0
    return res

@register.inclusion_tag('products/item.html', takes_context=True)
def show_item(context ,product):
    return { 
        'product': product
        }