class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        # 1. Находим цель (максимальный OR)
        max_or = 0
        for x in nums:
            max_or |= x
        
        n = len(nums)
        count = 0
        
        def backtrack(index, current_or):
            nonlocal count
            
            # Базовый случай: мы проверили все числа в массиве
            if index == n:
                if current_or == max_or:
                    count += 1
                return
            
            # Вариант А: Берем текущее число в подмножество
            # Обновляем current_or с помощью побитового ИЛИ
            backtrack(index + 1, current_or | nums[index])
            
            # Вариант Б: Не берем текущее число
            # current_or остается прежним
            backtrack(index + 1, current_or)
            
        # Запускаем рекурсию с первого элемента и нулевого OR
        backtrack(0, 0)
        
        return count
