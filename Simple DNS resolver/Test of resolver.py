from resolver.resolver import Resolver

resolve = Resolver()

print(resolve('facebook.com'))
print(resolve._cache)
