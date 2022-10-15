#Pagination Helper Code


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection=collection
        self.items_per_page=items_per_page
        

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
        

    # returns the number of pages
    def page_count(self):
        if len(self.collection) % self.items_per_page==0:
            return len(self.collection) // self.items_per_page
        else:
            return 1 + len(self.collection) // self.items_per_page
            

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        number_of_pages=PaginationHelper.page_count()
        items_per_page_list=[]
        for i in range(0,number_of_pages):
            if number_of_pages==1:
                items_per_page_list.append(PaginationHelper.item_count())
            else:
                if i!= number_of_pages-1:
                    items_per_page_list.append(self.items_per_page)
                else:
                    items_per_page_list.append(len(self.collection) % self.items_per_page)
        if page_index> number_of_pages:
            return -1
        else:
            return items_per_page_list[page_index]
            
                
            
            
        

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        index_per_page_list=[]
        for i in range(0,PaginationHelper.page_count()):
            page_index_list=[]
            
        
        
            
            
            
