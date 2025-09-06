import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        merged.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        merged.append(right[right_idx])
        right_idx += 1
    return merged

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    data_sizes = [100, 1000, 5000, 10000]
    num_runs = 5  # Кількість прогонів для timeit для кращої точності

    print(f"{'Data Size':<15}{'Data Type':<20}{'Merge Sort (s)':<20}{'Insertion Sort (s)':<20}{'Timsort (s)':<20}")
    print("-" * 95)

    for size in data_sizes:
        # Генерація даних
        random_data = [random.randint(0, 100000) for _ in range(size)]
        sorted_data = sorted(random_data) # Вже відсортовані дані
        reverse_sorted_data = sorted(random_data, reverse=True) # Зворотньо відсортовані дані

        datasets = {
            "Random": random_data,
            "Sorted": sorted_data,
            "Reverse Sorted": reverse_sorted_data
        }

        for data_type, data in datasets.items():
            merge_time = timeit.timeit(lambda: merge_sort(list(data)), number=num_runs)
            insertion_time = timeit.timeit(lambda: insertion_sort(list(data)), number=num_runs)
            timsort_time = timeit.timeit(lambda: sorted(list(data)), number=num_runs)

            print(f"{size:<15}{data_type:<20}{merge_time/num_runs:.6f}{'':<4}{insertion_time/num_runs:.6f}{'':<4}{timsort_time/num_runs:.6f}")

    print("\n" + "=" * 95)
    print("Висновки:")
    print("1. Timsort (вбудований `sorted()`) є найефективнішим алгоритмом сортування в більшості випадків, особливо для великих наборів даних та частково відсортованих масивів. Це підтверджує, що комбінація сортування злиттям та сортування вставками, а також оптимізації, роблять його дуже швидким.")
    print("2. Merge Sort показує стабільну продуктивність для різних типів даних, що відповідає його теоретичній складності O(N log N). Його ефективність є хорошою для великих масивів, але зазвичай повільнішою за Timsort через більші накладні витрати.")
    print("3. Insertion Sort є дуже ефективним для малих наборів даних або майже відсортованих даних. Однак, його продуктивність значно погіршується для великих і невпорядкованих наборів даних (O(N^2) в найгіршому випадку), що робить його непридатним для сортування великих масивів.")
    print("4. Емпіричні дані підтверджують теоретичні оцінки складності. Для великих масивів Timsort і Merge Sort значно перевершують Insertion Sort.")
    print("5. Отже, програмістам варто використовувати вбудовані функції сортування Python, оскільки вони реалізовані високоефективним Timsort-ом і оптимізовані для різних сценаріїв використання.") 