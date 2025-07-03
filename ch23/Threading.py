# from threading import Thread
# from time import sleep


# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("Ayush:")
#             sleep(3)


# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("Akhileshs")
#             sleep(3)


# t1 = A()
# t2 = B()
# # t1.run()  # start method
# # t2.run()  # start method
# t1.start()
# t2.start()
# from threading import Thread
# from time import sleep


# class A:
#     def run(self):
#         for i in range(5):
#             print("AYush Upadhyay:")
#         sleep(4)


# class B:
#     def run(self):
#         for i in range(5):
#             print("Amit Upadhyay")
#         sleep(4)


# t1 = A()
# t2 = B()

# t1.run()
# t2.run()

from threading import Thread

from time import sleep


class A(Thread):
    def run(self):
        for i in range(5):
            print("Ayush Upadhyay")
            sleep(4)


class B(Thread):
    def run(self):
        for i in range(5):
            print("Akhilesh Upadhyay")
            sleep(5)


t1 = A()
t2 = B()
# t1.run()
# t2.run()
t1.start()
t2.start()
