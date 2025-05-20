class PromptBuilder:
    @staticmethod
    def build_system_prompt(role: str):
        return f"You are a {role}. Follow the user's instructions carefully."

    @staticmethod
    def build_user_prompt(task: str, context: str = ""):
        if context:
            return f"Task: {task}\nContext: {context}"
        return f"Task: {task}"