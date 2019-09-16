import numpy as np

string_s = np.array(['1.25','-9.6'], dtype=np.string_)
print(string_s)
print(string_s.dtype)
string_f = string_s.astype(float)
print(string_f)
print(string_f.dtype)
