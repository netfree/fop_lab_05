from Student import Student

def run_Student_tests():
    test_init()
    test_name()
    test_id()
    test_group()

def test_init():
    Student(12, "Andrei", 10)
    Student()
    assert(Student().group == 0)
    
def test_name():
    try:
        Student(12, 12, 12)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "string expected")
        

def test_id():
    try:
        Student("asas", "Andrei", 12)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "int expected")
    

def test_group():
    try:
        Student(1, "Andrei", "Ana")
        assert(False)
    except Exception as ex:
        assert(str(ex) == "int expected")

    try:
        Student(1, "Andrei", -12)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "positive numeber expected")


        