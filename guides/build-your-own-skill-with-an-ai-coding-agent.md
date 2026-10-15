# Build Your Own Skill With an AI Coding Agent

**Start here:** Make an empty folder, open it in Claude Code or Codex, paste the brief below and answer its questions.

```text
I'm a salesperson, not a developer. Help me turn one task I repeat into a skill: a plain text instruction file you can follow every time. Work in this folder only. Go in this order, and stop and wait for my OK after each step:

1. Ask me what the task is, what a good result looks like, what you must never do or decide, and when you should refuse. Use fictional examples only. Don't ask for real customer information.
2. Write the skill as one file called SKILL.md. It needs a name, a description that says when not to use it, the inputs it needs, the steps, guardrails that each name a specific mistake, stop conditions, and what a person must check before using the result.
3. Write three fictional test cases as separate files: one ordinary, and two where the easy answer is wrong. In a separate file, write down what a good reply to each looks like, before anything is run.
4. Run the skill on each case in a fresh conversation, or tell me how to, and save each reply. Show me exactly where each reply went wrong, with quotes.
5. Suggest one change to the skill at a time. Don't change it until I say yes.

Never send, post or change anything outside this folder, and keep a list of what you did in a file called LOG.md. Ask me the first question now.
```

A coding agent can do more than answer a question. It can write files into a folder, run things and keep a log of what it did. That makes it a good partner for building a skill. It can write the skill, write the test cases and keep the record, and you decide at each stop. You don't need to write any code.

If you only want to turn a task into a skill in a chat, [Skill Author](https://github.com/shaunmarsden/skill-author) does that without any coding tool. This guide is for when you want the tests and the record as well.

## What Happens at Each Step

| Step | What the agent does | What you do |
| --- | --- | --- |
| 1. Questions | Asks what the task is, what a good result looks like, what it must never do and when it should refuse | Answer with made-up details, not real customers |
| 2. The skill | Writes `SKILL.md` with the parts a skill needs | Read it. Say yes or no to any rule it added that you didn't ask for |
| 3. Test cases | Writes three fictional cases and a separate file saying what a good reply looks like, before anything runs | Read the expected replies and fix any you disagree with |
| 4. Runs | Runs each case in a fresh conversation and marks each reply against the expected one, with quotes | Read the marking. Check anything it counted |
| 5. Changes | Suggests one change to the skill and waits | Say yes or no. The agent changes nothing until you do |

## What I Saw When I Tried It

I ran the brief three times in Claude on 15 October 2026, each time with an empty folder and the same made-up task, a follow-up email after a discovery call. The [test page](../evaluations/build-your-own-skill-brief-test.md) has the details. In short:

- **Every run stopped where the brief said to.** Each asked its questions one at a time, wrote the skill, stopped, wrote three cases, stopped, ran them, stopped and suggested one change without making it. Each kept a `LOG.md`.
- **Each wrote rules I hadn't asked for.** Three, four and four of them. Each flagged them for my yes or no. That's the stop at step 2 doing its job.
- **The test cases found real gaps.** One run found a check item that read as the opposite of what it meant. Another found that the skill said nothing about a next step given as a week and not a day, such as "w/c 3 Nov". A third found that the skill told me to leave out two things I'd promised the prospect, and didn't say what to do about the promises.
- **Two of the three miscounted words.** The skill says to keep the email under 150 words, and the helper's own count of its email was off by three to six words in those runs. If a limit matters, count it yourself.
- **Every reply passed the three cases.** The cases were mine and so was the skill, so that shows the skill works for those cases, not that it has no gaps. The gaps above are why.

## Why the Cases Come Before the Runs

Write down what a good reply looks like before you run anything, and make two of your three cases ones where the easy answer is wrong. The test I ran on the [outbound prospecting skill and prompt](../evaluations/outbound-qualification-stop-test.md) shows why. The prompt had no stop for a company outside the profile, and it wrote a message for every such company. The skill had the stop and wrote none. A case where the easy answer is right wouldn't have shown it.

## What Stays With You

The agent drafts and tests. You decide, and you send. The brief tells it to work in one folder and to send nothing, and its log shows what it did. Don't put real customer names, transcripts or prices in the folder. Use [the private context route](../context/README.md) for anything real, and keep real customer material in your company's approved systems.

## This Repository Is the Worked Case

This repository is built the same way. Each skill sits in its own folder, each test writes its expected result before any run, and a script checks the links and the style. When I change something, the agent opens a draft pull request and I'm the only one who merges it. The [guide to running this repository with a coding agent](run-this-repository-with-an-ai-coding-agent.md) shows the one sentence that sets that up.

## What I Can't Tell

- **I tried Claude only.** I haven't tried Codex. Both read an instruction file in the folder, but I haven't compared them.
- **I played the user.** I wrote the answers, so the brief wasn't tested on someone who didn't know what it was for. I haven't had a salesperson who isn't me run it.
- **Three runs on one task.** A different task, or a longer one, could go differently.
- **The agents worked inside my setup,** which includes my project notes. A fresh install may behave a little differently.
- **Tools change.** Treat the steps as the shape of the job, not a promise about any one product.
