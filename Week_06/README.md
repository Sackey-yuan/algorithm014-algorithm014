学习笔记
1、递归代码
# python
def recursion(level, param1, param2...):
    # recursion terminator
    if leve > maxLevel:
        process_result
        return result
    # process logic  in current level
    process(level, param1, param2...)
    # drill down
    recursion(level + 1, p1, p2...)
    #reverse the current level status if need
2、分支代码模板
# python
def divider_conquer(problem, param1, param2...):
    # recursion terminator
    if problem is None:
        print(result)
        return
    # prepare data
    data = prepare_data(problem)
    sub_problems = split_problem
    # conquer sub_problem
    sub_result1 = self.divider(sun_problem[0], p1, p2...) 
    sub_result2 = self.divider(sun_problem[1], p1, p2...) 
    sub_result3 = self.divider(sun_problem[2], p1, p2...) 
    ...
    # process and generate the final result
    result = process_result(sun_result1, sun_result2, sun_result3...)
    #reverse the current the level status if need
    
3,动态规划模板dp_function:
def dp_function():
    # 特殊条件
    if result == None:
        return None
    # 生产dp空间
    dp = [] * need
     # 递推
    for i in range(need):
        # do dp_function
        dp[i] = dp_function(dp[i-1],dp[i-2]...)   
    return dp[-1]
    