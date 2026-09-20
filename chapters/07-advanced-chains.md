# Chapter 7 — advanced chains and capstones

## 7.1 Constraint-first exploitation

Advanced work is not a bag of tricks. Begin with the objective and list constraints: input bytes, available reads, writable memory, mappings, mitigations, allowed syscalls, process lifetime, and success output. Select the smallest primitive that satisfies the next dependency.

## 7.2 seccomp and SROP concepts

The `seccomp-rop` fixture teaches syscall inventory and `no_new_privs` without modifying the host kernel. Use `strace -f` to observe startup and normal execution. A filtered target requires a chain made only from allowed operations. SROP is a register-setting technique based on a crafted signal frame; it is powerful because one kernel-restored frame can set many registers, but the frame address and syscall path must be proven.

## 7.3 Dynamic linking and loader reasoning

The PLT, GOT, relocations, and loader form another state machine. Lazy binding can make a first call different from later calls; full RELRO changes when relocation data becomes writable. Read the relevant disassembly and relocation entries instead of assuming a textbook layout.

## 7.4 Capstone workflow

For each capstone, submit four artifacts:

1. **Evidence log:** commands, crash/leak transcript, architecture, and mitigation state.
2. **Primitive statement:** what capability the bug grants and what it cannot do.
3. **Chain table:** each stage, input constraint, address source, and verification.
4. **Writeup:** root cause, exploit, reliability, and defensive repair.

Use assertions in the exploit:

```python
assert context.arch == 'amd64'
assert leak & 0xfff == expected_alignment
io.recvuntil(b'prompt: ')
```

## Mastery standard

You have mastered the material when you can start from an unfamiliar local binary, derive a chain without copying a payload, explain why mitigations do or do not block it, run it repeatedly, and repair the bug. The final test is communication: another learner should be able to reproduce your evidence from the writeup.

## Capstone progression

### Capstone A — guided stack chain

You receive source, a non-PIE binary, and a visible `win` function. Submit the offset calculation, a ret2win exploit, and a patched source. This checks that you can move from crash to controlled return.

### Capstone B — leak plus ROP

The target exposes a pointer but not a final target address. You must identify the mapping, calculate a base, preserve the process, and send a second stage. Submit a chain table and five successful local runs.

### Capstone C — format string plus control flow

Use a format-string disclosure to recover a useful pointer, then choose either a controlled write or a ROP path. You must explain positional arguments and newline constraints rather than submitting a generated payload alone.

### Capstone D — heap lifetime chain

The menu contains allocation, deletion, editing, and display operations. Find the lifetime error, demonstrate reuse, and decide whether the resulting primitive is a read, write, or callback control. Your solution must state the glibc version it expects.

## Submission template

```text
Artifact: challenge name and sha256
Environment: WSL distribution, gcc, glibc
Root cause: file/function/operation
Primitive: capability and limitations
Stage 1: input and evidence
Stage 2: calculation and invariant
Final stage: control and success marker
Reliability: number of repeated successes
Repair: source change and regression result
```

If you cannot fill in one line, the exploit is not finished. The missing line tells you what to investigate next.
