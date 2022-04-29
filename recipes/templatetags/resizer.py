from django import template

register = template.Library()

def resize_to(value, arg):
  print("value:", value)
  print("arg:", arg)
  return "resize done"


register.filter(resize_to)