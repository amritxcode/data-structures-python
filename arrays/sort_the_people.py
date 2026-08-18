class Solution:
    def sort_people(self, names:list[str], heights:list[int])->list[str]:
        pairs = sorted(zip(heights, names), reverse = True)

        sorted_names = []
        for height, name in pairs:
            sorted_names.append(name)

        return sorted_names