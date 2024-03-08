
# The general principal behind dancing links is as follows:
# L[x] ~ The pointer to the element on the left of element x (still contained within the x element data structure)
# R[x] ~ The pointer to the element on the right of element x (still contained within the x element data structure)
# L[R[x]] ~ The the pointer to the element that element R[x] points to, which is on its left.
# R[L[x]] ~ The the pointer to the element that element L[x] points to, which is on its right.
# L[R[x]] <- L[x] ~ Replace the pointer of L[R[x]] to point to the element to the left of element x
# R[L[x]] <- R[x] ~ Replace the pointer of R[L[x]] to point to the element to the right of element x
# 2a.) L[R[x]] <- x ~ Replace the pointer of L[R[x]] to point to element x
# 2b.) R[L[x]] <- x ~ Replace the pointer of R[L[x]] to point to element x
# 2a and 2b work because we dont remove x from the list and it just
# sits in purgatory. In theory we could free x but in many cases it
# would sit between memory addr(L[x] + sizeof(L[x])) and addr(R[x]).
# Unless sizeof(x) is a page large and is page aligned, forget it...
# Another option would be to shift all elements over but this is really
# compute intensive and wastes precious cpu cycles :)


