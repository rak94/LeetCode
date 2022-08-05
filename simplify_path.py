class SimplePath:
    def simplify_path(self, path: str) -> bool:
        stack = []
        curr = ""

        for c in path + "/":
            if curr == "/":
                if curr == "..":
                    if stack: stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += c
        return "/" + "/".join(stack)