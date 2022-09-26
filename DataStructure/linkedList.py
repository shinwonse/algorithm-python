# Node 정의
class Node:
    def __init__(self, data, next):  # 데이터를 담는 data, 후임 노드를 가리키는 next
        self.data = data
        self.next = next


# 링크드리스트 정의
class LinkedList:
    def __init__(self):
        self.no = 0  # 링크드리스트의 길이
        self.head = None  # 머리 노드
        self.current = None

    def __len__(self):
        return self.no

    # 링크드리스트에서 데이터 검색 후
    # 데이터가 발견되면 그 위치를 반환하고, current 값을 해당 노드로 바꾼다
    # 검색 실패시 -1을 반환
    def search(self, data):
        count = 0
        pointer = self.head
        while pointer is not None:
            if pointer.data == data:
                return count
            count += 1
            pointer = pointer.next
        return -1

    # 데이터가 링크드리스트에 포함되어 있는지 판단
    # search 메서드를 호출하고 그 반환 값이 0 이상이면 포함으로 판단
    def __contains__(self, data):
        return self.search(data) >= 0

    # 링크드리스트 맨 앞에 노드 추가
    def add_first(self, data):
        pointer = self.head
        self.head = Node(data, pointer)
        self.no += 1

    # 링크드리스트 맨 뒤에 노드 추가
    def add_last(self, data):
        pointer = self.head
        # 링크드리스트가 비어있으면
        if pointer is None:
            self.add_first(data)
        else:
            # 꼬리 노드 탐색
            while pointer.next is not None:
                pointer = pointer.next

            pointer.next = Node(data, None)
            self.no += 1

    # 링크드리스트 맨 앞 노드 삭제
    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next
            self.no -= 1

    # 링크드리스트 맨 뒤 노드 삭제
    def remove_last(self):
        if self.head.next is None:
            self.remove_first()
        else:
            cur_pointer = self.head
            pre_pointer = self.head
            while cur_pointer.next is not None:
                pre_pointer = cur_pointer
                cur_pointer = cur_pointer.next

            pre_pointer.next = None
            self.no -= 1

    # 링크드리스트 특정 데이터 삭제
    def remove(self, data):
        if self.head is not None:
            # 그게 맨앞 데이터면 맨앞 데이터 삭제
            if self.head.data == data:
                self.remove_first()
                return True

            # 맨앞 데이터가 아니면 헤드에 포인터를 두고
            pointer = self.head
            # 끝까지 탐색
            while pointer.next is not None:
                if pointer.next.data == data:
                    pointer.next = pointer.next.next
                    return True
                pointer = pointer.next
        return False

    # 이터레이터 객체로 만들기
    # __iter__ 메서드를 가지고 있는지 확인하기
    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        # 오류 발생
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data


ll = LinkedList()

ll.add_last("a")
ll.add_last("b")
ll.add_last("c")
ll.add_last("d")

for item in ll:
    print(item)
