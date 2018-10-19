# Align to left with spaces only
print('Align to left with spaces only')
print('{:10}'.format('test'))

# Align to Right with spaces only
print('Align to Right with spaces only')
print('{:>10}'.format('test'))

# Align to left and concatenate with a symbol '_'
print('{:_<10}'.format('test'))

# Align to Right and concatenate with a symbol '_'
print('{:_>10}'.format('test'))

# Align to Right and concatenate with a symbol '*'
print('{:{}>10}'.format('test', '*'))


# Align to Right and concatenate with a symbol '*'
print('{:{}^10}'.format(' test ', '*'))
