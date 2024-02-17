class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # İki listeyi birleştir ve sırala
        sum_nums = sorted(nums1 + nums2)
        # Listelerin toplam uzunluğunu bul
        n = len(sum_nums)
        
        # Medyanı bul
        if n % 2 == 1:  # Eğer toplam uzunluk tek ise, ortadaki eleman medyandır
            median = sum_nums[n // 2]
        else:  # Eğer toplam uzunluk çift ise, ortadaki iki elemanın ortalaması medyandır
            median = (sum_nums[n // 2 - 1] + sum_nums[n // 2]) / 2
        
        return median
