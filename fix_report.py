import re

with open("webvulnscan.py", "r", encoding="utf-8") as f:
    code = f.read()

# نعدل الجزء اللي بيعرض info
old = '''                for i, issue in enumerate(issues, 1):
                    print(f"{color}{i}. {issue['type']}{Style.RESET_ALL}")
                    print(f"   📝 {issue['description']}")
                    if 'url' in issue:
                        print(f"   🌐 URL: {issue['url']}")
                    if 'payload' in issue:
                        print(f"   ⚡ Payload: {issue['payload']}")
                    if 'header' in issue:
                        print(f"   🏷️  Header: {issue['header']}")
                    print(f"   🛠️  Solution: {issue['solution']}")
                    print()'''

new = '''                for i, issue in enumerate(issues, 1):
                    if isinstance(issue, str):
                        print(f"{color}{i}. {issue}{Style.RESET_ALL}")
                        print()
                    else:
                        print(f"{color}{i}. {issue.get('type', 'Issue')}{Style.RESET_ALL}")
                        print(f"   📝 {issue.get('description', '')}")
                        if 'url' in issue:
                            print(f"   🌐 URL: {issue['url']}")
                        if 'payload' in issue:
                            print(f"   ⚡ Payload: {issue['payload']}")
                        if 'header' in issue:
                            print(f"   🏷️  Header: {issue['header']}")
                        print(f"   🛠️  Solution: {issue.get('solution', '')}")
                        print()'''

if old in code:
    code = code.replace(old, new)
    with open("webvulnscan.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("✅ تم الإصلاح")
else:
    print("⚠️ لم أجد الكود — نحاول طريقة أخرى")
