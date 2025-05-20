import ui
import ai
import core

def main():
  ui.init()
  user_prompt = getUserPrompt()
  final_prompt = AI.generate_prompt(user_prompt)
  sys_feat = AI.submit_prompt(final_prompt)
  results = core.execute_scan(core.features[sys_feat])
  friendly_results = AI.gen_friendly_output(results)
  UI.update()
