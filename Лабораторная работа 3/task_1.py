def search_item(lis, item):
    if item in lis:
        return lis.index(item)
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
Item =[input('')]
for find_item in Item :
    index_item = search_item(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")