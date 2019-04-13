from builtins import print

import tensorflow as tf

# 1차원 리스트 할당 5.0 ~5.9 까지의 무한대 따라서 float가 기본 값이다.
var = tf.Variable([5.0], dtype=tf.float32)   # 대문자로 시작 ---> 객체
con = tf.constant([10.0], dtype=tf.float32)  # 소문자로 시작 ---> 상수
session = tf.Session()
init = tf.global_variables_initializer()

session.run(init)
print(session.run(var * con))  # 50.

print('-------------------------------------------------------')

session.run(var.assign([10.0]))
print(session.run(var)) # 10.

p1 = tf.placeholder(dtype=tf.float32)
p2 = tf.placeholder(dtype=tf.float32)

t1 = p1 * 3
t2 = p1 * p2
# 값의 변화를 주기 위해서는 반드시 session.run() 안에서 해 주어야 한다.
print(session.run(t2, feed_dict={p1:4.0, p2:[2.0, 5.0]}))  # 8. 20.

# t1 을 이용해서 12.0를 출력하세요.
print(session.run(t1, {p1:[4.0]}))


