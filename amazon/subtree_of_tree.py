def is_subtree(self, s, t) -> bool:
    def is_match(s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False
        return is_match(s.left, t.left) and is_match(s.right, t.right)

    if s is None:
        return False
    return is_match(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
