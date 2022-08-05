# bad solution, would be cooler to check error conditions beofre iterreratng the problems, anyway ...

def arithmetic_arranger(problems, ans=False):
    print(problems)
    top = []
    bot = []
    lin = []
    cal = []
    first = True
  
    # check lens
    if len(problems) > 5:
      return 'Error: Too many problems.'

    # loop problems
    for i in problems:
      top_tmp, oper_tmp, bot_tmp = i.split(' ') 

      # check operator
      if oper_tmp == '*' or oper_tmp == '/':
        return 'Error: Operator must be \'+\' or \'-\'.'

      # check if digits
      if not (top_tmp.isdigit() and bot_tmp.isdigit()): 
        return 'Error: Numbers must only contain digits.'

      # check len from digits
      if len(top_tmp) > 4 or len(bot_tmp) > 4:
        return 'Error: Numbers cannot be more than four digits.'

      if oper_tmp == '+':
        cal_tmp = str(int(top_tmp) + int(bot_tmp))
      else:
        cal_tmp = str(int(top_tmp) - int(bot_tmp))


      if len(top_tmp) <  5 and len(bot_tmp) >5:
        len_tmp = 4
      elif len(top_tmp) > len(bot_tmp):
        len_tmp = len(top_tmp) + 2
      else:
        len_tmp = len(bot_tmp) + 2

      if not first:
        bot.append('    ')
        top.append('    ')
        lin.append('    ')
        cal.append('    ')
      else:
        first = False
      
      bot.append(oper_tmp + f'{bot_tmp:>{len_tmp-1}}')
      top.append(f'{top_tmp:>{len_tmp}}')
      lin.append('-'*len_tmp)
      if ans:
        cal.append(f'{cal_tmp:>{len_tmp}}')  
    
    if ans:
      return ("".join(top)+'\n'+"".join(bot)+'\n'+"".join(lin)+'\n'+"".join(cal))
    else:
      return ("".join(top)+'\n'+"".join(bot)+'\n'+"".join(lin))
      
    
    # return arranged_problems
