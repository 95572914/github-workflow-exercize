from app.app import dedupe_list

def test_dedupe_list():
    # 测试正常列表去重
    assert dedupe_list([1, 2, 2, 3]) == [1, 2, 3]
    # 测试空列表
    assert dedupe_list([]) == []
    # 测试单元素列表
    assert dedupe_list([5]) == [5]