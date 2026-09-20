# Writeup: find-the-offset

The vulnerable read reaches saved control data after compiler-introduced frame state. The correct offset is an observed value from the target build, not a universal constant. Record the pattern, faulting register, and calculated offset; then verify with a marker payload.

