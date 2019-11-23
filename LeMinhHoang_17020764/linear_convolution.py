import numpy as np
#tính linear convolution trực tiếp
def convolvetest(a, b):
    longer = [a, b][np.argmax((len(a), len(b)))]
    shorter = [b, a][np.argmin((len(b), len(a)))]
    K = len(longer)-len(shorter)+1
    convolution = np.zeros(K, longer.dtype)
    for i in range(K):
        convolution[i] = np.dot(longer[i:len(shorter)+i], shorter[::-1])
    return convolution
# def convolvetest(a, w, b = 0, stride = 1, pad = 0):
#     """
#     compute 1d convolutional (with bias)
#     """
#     w_old = a.shape[0]
#     f = w.shape[0]
#     a_pad = np.pad(a, pad_width=pad, mode = 'constant', constant_values = 0)
#     w_new = int((w_old - f + 2*pad)/stride) + 1
#     a_res = np.zeros((w_new))
#     for i in range(w_new):
#         start = i*stride
#         end = start + f
#         a_res[i] = np.sum(a_pad[start:end]*w) + b
#     return a_res

# a = np.random.normal(0.0, 1.0, 100)
# b = np.random.normal(0.0, 1.0, 11)
a = np.array([1,2,3])
b = np.array([3,4,5])
#Hàm có sẵn convolve của python tính linear convolution
# print(np.allclose(np.convolve(a, b, mode='same'),
#             convolvetest(np.pad(a, ((len(b)-1)/2, (len(b)-1)/2), mode='constant', constant_values=0.0), b)))
print(np.allclose(np.convolve(a, b, mode='same'), convolvetest(a, b)))
print(a)
print(b)
print(convolvetest(a,b))