import  numpy as np
import  tensorflow as tf


x_data=np.random.rand(100).astype(np.float32)

y_data=x_data*0.1+0.3


#start

Weight=tf.Variable(tf.random_uniform([1],-1,1))
baise=tf.Variable(tf.zeros([1]))

y=Weight*x_data+baise


loss=tf.reduce_mean(tf.square(y-y_data))
optimizer=tf.train.GradientDescentOptimizer(0.5)
train=optimizer.minimize(loss)


init=tf.global_variables_initializer()
#init=tf.initialize_all_variables()
#end

sess=tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step%20 == 0:
        print(step,sess.run(Weight),sess.run(baise))
