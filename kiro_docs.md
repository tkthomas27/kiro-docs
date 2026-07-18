# Kiro IDE Comprehensive Documentation
*Compiled on July 18, 2026*

---
# Get Started

Kiro is an agentic IDE that helps you do your best work with features such as specs, steering, and hooks.

### Get started

Everything you need to begin your journey with Kiro in under 5 minutes.

[Download & InstallGet Kiro running on your machine](https://kiro.dev/docs/getting-started/installation/)[First ProjectLearn about Kiro's features through a hands-on project](https://kiro.dev/docs/getting-started/first-project/)

### Core capabilities

Learn about Kiro's core feature set.

[SpecsPlan and build features using structured specifications.](https://kiro.dev/docs/specs/)[HooksAutomate repetitive tasks with intelligent triggers.](https://kiro.dev/docs/hooks/)[Agentic chatBuild features through natural conversation with AI.](https://kiro.dev/docs/chat/)[SteeringGuide AI with custom rules and context.](https://kiro.dev/docs/steering/)[MCP ServersConnect external tools and data sources.](https://kiro.dev/docs/mcp/)[Privacy FirstKeep code secure with privacy controls.](https://kiro.dev/docs/privacy-and-security/)

### Learning resources

Master Kiro through hands-on tutorials and comprehensive documentation.

[Your first projectA quick overview of how to use Kiro's feature set.](https://kiro.dev/docs/getting-started/first-project/)[Interactive TutorialBuild a real project while learning Kiro's features through our game-based tutorial](https://kiro.dev/docs/guides/learn-by-playing/)Page updated:  May 28, 2026[Installation](https://kiro.dev/docs/getting-started/installation/)

---

# Installation

### System Requirements

Kiro is available for macOS, Windows, and Linux.

- On macOS, Kiro runs on both Intel and Apple silicon with the latest security updates.

- On Windows, Kiro supports Windows 10 and 11 (64-bit only). ARM is not currently supported.

- On Linux, Kiro requires glibc 2.39 or higher. For example Ubuntu 24+, Debian 13+, Fedora 40+, Arch Linux, and Linux Mint 22+.

### Download Kiro

1. Go to [kiro.dev](https://kiro.dev) and download the installer

1. Open the downloaded file and follow the installation instructions for your operating system (Windows, macOS, or Linux).

1. Open Kiro IDE and start coding!

### First run

1. When you open Kiro for the first time you will be asked to login with a provider of your choice that include social and AWS login options. Learn more about the [auth methods](https://kiro.dev/docs/getting-started/authentication).

1. Once logged in, you can choose to [import your VS Code](https://kiro.dev/docs/guides/migrating-from-vscode) settings and extensions. If you're using another editor, you can skip this step. Select your preferred theme from the available options, then allow Kiro to set up shell integration, enabling the agent to execute commands on your behalf.

1. Finally, you'll arrive at the welcome page. Open a project to get started and proceed with [your first project](https://kiro.dev/docs/getting-started/first-project).

[View transcript: Kiro IDE initial setup demo video](https://kiro.dev/transcripts/kiro-3/)

### Downgrade to a previous version

You can revert to an earlier version of Kiro if an update introduces issues with your workflow.

1. Go to the [downloads page](https://kiro.dev/downloads)

1. Scroll past the main download cards to the version list

1. Expand the version you want to install (for example, "IDE 0.12.x")

1. Download the installer for your platform

1. Uninstall your current version of Kiro:


    - **macOS:** drag Kiro from Applications to the Trash

    - **Windows:** uninstall from **Settings > Apps > Installed apps**

    - **Linux:** run `sudo apt remove kiro` or `sudo dnf remove kiro` depending on your package manager

1. Run the downloaded installer

Your settings, extensions, and sign-in state are preserved across reinstalls. When you're ready to move back to the latest version, download it from the [downloads page](https://kiro.dev/downloads) or let the application update automatically.

### Language support

Kiro supports most popular programming languages. These guides cover environment setup and best practices:

- [TypeScript and JavaScript](https://kiro.dev/docs/guides/languages-and-frameworks/typescript-javascript-guide)

- [Java](https://kiro.dev/docs/guides/languages-and-frameworks/java-guide)

- [Python](https://kiro.dev/docs/guides/languages-and-frameworks/python-guide)

Page updated:  June 25, 2026[Authentication](https://kiro.dev/docs/getting-started/authentication/)

---

# First Project

This guide walks you through Kiro's essential features by working with a real project. You'll learn how to use steering files, specs, hooks, and MCP servers to enhance your development workflow.

### Prerequisites

Before starting, ensure you have:

- [Installed Kiro](https://kiro.dev/docs/getting-started/installation).

- A project to work with (either an existing project or a new one)

- Basic familiarity with your project's structure and technology stack

### Open your project

1. **Launch Kiro** and open your project:




    - Use `File > Open Folder` to select your project directory

    - Or drag and drop your project folder into Kiro

    - Or go to the command line and run `kiro .` from your project directory

1. **Access the Kiro Panel**:




    - Click the Kiro Ghost icon in the activity bar (left sidebar)

    - This panel provides access to all of Kiro's AI-powered features

1. **Start a Chat Session**:




    - The chat pane should be open by default

    - This opens Kiro's conversational interface where you can interact with the AI

[View transcript: Opening the Kiro chat pane](https://kiro.dev/transcripts/kiro-pane/)

### Set up Steering files

Steering files provide context about your project, helping Kiro understand your codebase, conventions, and requirements.

[View transcript: Generating steering documents in Kiro](https://kiro.dev/transcripts/kiro-steering/)

To get started choose `Generate Steering Docs` from the Kiro pane. Kiro generates project steering documents for you stored in `.kiro/steering/` that guide Kiro's behavior. They contain information about:

- Your product and its purpose

- Technical stack and frameworks

- Project structure and conventions

You can also create custom steering files by clicking the `+` button in the steering section and add things like coding standards, and workflows, and team best practices. Learn about steering [here](https://kiro.dev/docs/steering/).

### Build features with Specs

Specs transform high-level feature ideas into detailed implementation plans through three phases:

1. **Requirements** - User stories with acceptance criteria in EARS notation

1. **Design** - Technical architecture and implementation approach

1. **Tasks** - Discrete, trackable implementation steps

#### Create your first Spec

[View transcript: Creating a spec in Kiro](https://kiro.dev/transcripts/specs-start/)

1. **Start a New Spec**:




    - In your chat session, click the **Spec** button

    - Choose the `+` button in the Kiro panel's Specs section

1. **Enter a feature description**:




    - Describe your feature in natural language

    - Example: "Add a user authentication system with login, logout, and password reset functionality"

1. **Follow the Guided Workflow**:




    - **Requirements Phase**: Kiro will help structure your requirements using EARS notation

    - **Design Phase**: Technical architecture and component design will be documented

    - **Implementation Phase**: Discrete tasks will be generated for execution

#### Execute Spec tasks

Once your spec is complete:

1. **Review Generated Tasks** in the `tasks.md` file

1. **Execute Tasks** by clicking on individual task items

1. **Track Progress** as tasks automatically update to "In Progress" and "Done"

### Automate workflows with Hooks

Agent Hooks eliminate manual work by automatically executing predefined actions when:

- Files are created, saved, or deleted

- Manual triggers are activated

- Specific file patterns are modified

To get started:

1. **Access Hook Creation**:




    - Navigate to the **Agent Hooks** section in the Kiro panel

    - Click the `+` button to create a new hook

1. **Define Hook Behavior**:




    - Describe what you want automated in natural language

    - Example: "When I save a React component file, automatically create or update its corresponding test file"

1. **Configure Hook Settings**:




    - **Event Type**: Choose when the hook triggers — file events (created, saved, deleted), prompt and agent lifecycle events (prompt submit, agent stop, pre/post tool use), spec task events (pre/post task execution), or manual trigger

    - **File Pattern**: Specify which files should trigger the hook (e.g., `src/**/*.tsx`)

    - **Instructions**: Define the specific actions to perform

[View transcript: Creating an agent hook in Kiro](https://kiro.dev/transcripts/hooks/)

### Extend capabilities with MCP

Model Context Protocol (MCP) allows Kiro to:

- Access specialized knowledge bases and documentation

- Integrate with external APIs and services

- Use domain-specific tools and utilities

- Connect to databases and cloud services

#### Set up MCP

1. Open the Kiro panel by clicking the Kiro Ghost icon in the activity bar. First enable MCPs, and then click the edit button (pencil icon) next to MCP in the panel

1. By default, Kiro ships with the [fetch MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) in the JSON file. Flip it to `disabled=false` to connect to it.

1. You can also **Add any MCP Server** by asking Kiro to add a new server or editing the JSON file directly:




    ```json
    {
      "mcpServers": {
        "web-search": {
          "command": "uvx",
          "args": ["mcp-server-brave-search"],
          "env": {
            "BRAVE_API_KEY": "your-api-key-here"
          },
          "disabled": false,
          "autoApprove": ["search"]
        }
      }
    }
    ```

#### Use MCP tools

Once configured, you can use MCP tools in several ways:

- **Direct Questions**


    - Ask questions that leverage the MCP server's capabilities:

    - Example: `Search for the latest React 18 best practices`

- **Explicit Tool Usage**


    - Reference specific MCP tools with the #MCP context provider

    - Example: `#[fetch] fetch` Use the web search to find examples of TypeScript generic constraints`

- **Integration with Other Features**


    - Combine MCP with hooks and specs:

    - Example: `Create a hook that uses the web search MCP to find relevant documentation when I create new component files`

### Next steps

Now that you've experienced Kiro's core features:

- **Try the Interactive Tutorial**: Work through our [hands-on game development tutorial](https://kiro.dev/docs/guides/learn-by-playing)

- **Learn more about specs**: Check out the [specs documentation](https://kiro.dev/docs/specs) to learn more about the concepts and how they work

- **Join the Community**: Connect with other Kiro users and share your experiences on our [Discord server](https://discord.gg/kirodotdev)

Page updated:  June 25, 2026[Authentication](https://kiro.dev/docs/getting-started/authentication/)[What's new in IDE 1.0](https://kiro.dev/docs/whats-new-1-0/)

---

# Chat Interface

Kiro offers a chat panel where you can interact with your code through natural language conversations. Just tell Kiro what you need. Ask questions about your codebase, request explanations for complex logic, generate new features, debug tricky issues, and automate repetitive tasks—all while Kiro maintains complete context of your project.

[View transcript: Tour of the Kiro chat panel](https://kiro.dev/transcripts/kiro-agent/)

### Key features

[Contextual UnderstandingAsk questions about your entire codebase, get explanations, or request edits with full awareness of your project structure](https://kiro.dev/docs/chat/vibe/)[Smart Intent DetectionKiro intelligently determines whether you want information or action, adapting its responses to match your workflow needs](https://kiro.dev/docs/chat/autopilot/)[Vibe vs Spec sessionsChat sessions can be either vibe or spec sessions. Learn more about the differences between these two.](https://kiro.dev/docs/chat/vibe/)[Dev ServersRun long-running processes in the background without blocking your workflow](https://kiro.dev/docs/chat/dev-servers/)

### Getting started

#### Accessing chat

There are multiple ways to access the chat in your development environment:

1. **Keyboard Shortcut**: Press `Cmd+L` (Mac) or `Ctrl+L` (Windows/Linux) to open the chat panel

1. **Command Palette**: Press `Cmd+Shift+P` (Mac) or  `Ctrl+Shift+P` (Windows/Linux) and search for `"Kiro: Open Chat"`

1. **Secondary Side Bar**: Click the Kiro chat icon toggle using `Cmd+Opt+B` (Mac) or `Ctrl+Alt+B` in the top bar on the right to open the chat panel

#### Multi-language support

Kiro chat supports conversations in multiple natural languages. Supported languages include Mandarin, French, German, Italian, Japanese, Spanish, Korean, Hindi, and Portuguese, with more languages available. You can start a conversation in your preferred language, and Kiro will automatically detect it and respond in the same language. This capability is powered by the underlying large language model (LLM) used.

#### Your first conversation

Once the chat panel is open:

1. Type your question or request in natural language in the chat input

1. Press Enter to send your message

1. Kiro will analyze your request and respond appropriately

Example requests to get started:

**Ask about your code**

```
"Explain how authentication works in this project"
```

**Generate new code**

```
"Create a React component for a user profile page"
```

**Fix issues**

```
"Help me fix the error in this function"
```

#### Exporting a conversation

To export a chat conversation with Kiro, right-click the tab of the conversation you wish to export and select **Export Conversation**. This will export the conversation in markdown (.md) format.

#### Smart intent detection

Kiro intelligently analyzes your messages to understand whether you want information or action. When you ask questions like "How does this work?" or "What's the purpose of this code?",
Kiro recognizes this as an information request and responds with explanations and documentation without modifying your code. When you use directives like "Create a component" or "Fix this bug", Kiro identifies this as an action request and will propose or implement the necessary code changes, execute commands, or manage files accordingly. This seamless intent recognition allows for natural conversation without requiring explicit commands to switch between information and action modes.

### Context management

Kiro's power comes from its deep understanding of your codebase context. It automatically analyzes open files in the editor, including their dependencies and structure, but you can also explicitly provide additional context.

#### Context providers

Use the `#` symbol in the chat input to access context providers:

| Provider | Description | Example |
| --- | --- | --- |
| `#codebase` | Allow Kiro to automatically find relevant files across your project | `#codebase explain the authentication flow` |
| `#file` | Reference specific files in your codebase | `#auth.ts explain this implementation` |
| `#folder` | Reference a specific folder and its contents | `#components/ what components do we have?` |
| `#git diff` | Reference the current Git changes | `#git diff explain what changed in this PR` |
| `#terminal` | Include recent output from your active terminal and command history | `#terminal help me fix this build error` |
| `#problems` | Include all problems in the current file | `#problems help me resolve these issues` |
| `#url` | Include web documentation | `#url:https://docs.example.com/api explain this API` |
| `#code` | Include specific code snippets in the context | `#code:const sum = (a, b) => a + b; explain this function` |
| `#repository` | Include a map of your repository structure | `#repository how is this project organized?` |
| `#current` | Reference the currently active file in the editor | `#current explain this component` |
| `#steering` | Include specific steering files for guidance | `#steering:coding-standards.md review my code` |
| `#docs` | Reference documentation files and content | `#docs:api-reference.md explain this API endpoint` |
| `#spec` | Reference all files from a specific spec (requirements, design, tasks) | `#spec:user-authentication update the design file to include password reset flow` |
| `#mcp` | Access MCP tools, prompts, and resource templates from connected servers | `#mcp:aws-docs how do I configure S3 buckets?` |

You can combine multiple context providers in a single request:

```
#codebase #auth.ts explain how authentication works with our database
```

**Tip**

The `#terminal` context provider is particularly powerful for debugging and troubleshooting. When you include `#terminal` in your message, Kiro can access your recent command history, outputs, and error messages to provide targeted assistance.

**Common scenarios:**

- **Build failures**: `#terminal My build is failing, what's the issue?`

- **Test debugging**: `#terminal These tests aren't passing, help me understand why`

- **Git issues**: `#terminal I'm stuck on this merge conflict`

- **Dependency problems**: `#terminal npm install is throwing errors`

Kiro can analyze the actual terminal output, understand error patterns, and suggest specific solutions based on what happened in your terminal session. For detailed examples and best practices, see the [Terminal Integration guide](https://kiro.dev/docs/chat/terminal).

### Sessions and history

Kiro maintains conversation history within sessions, allowing for continuous context-aware interactions.

#### Managing sessions

- **Create New Sessions**: Start fresh conversations for different topics or projects. Click on `+` icon in the chat panel to start a new session

- **Switch between Sessions**: Easily navigate between ongoing conversations through the tab switcher

- **View History**: Access previous interactions and their outcomes through the `History` button

- **Task Tracking**: Monitor the progress of ongoing and completed tasks through the `Task list` button

#### Execution history

Kiro maintains a detailed history of sessions that includes actions taken such as code changes, commands executed,
search results, file operations, and more. You can search, restore, or delete a specific session.

Loading image...![Kiro Execution History](https://kiro.dev/images/kirohistory.png?h=268115f8)Page updated:  June 25, 2026[Best practices](https://kiro.dev/docs/specs/best-practices/)[Autopilot](https://kiro.dev/docs/chat/autopilot/)

---

# Steering & Guidance

### What is steering?

Steering gives Kiro persistent knowledge about your workspace through markdown files. Instead of explaining your conventions in every chat, steering files ensure Kiro consistently follows your established patterns, libraries, and standards.

### Key benefits

**Consistent Code Generation** - Every component, API endpoint, or test follows your team's established patterns and conventions.

**Reduced Repetition** - No need to explain workspace standards in each conversation. Kiro remembers your preferences.

**Team Alignment** - All developers work with the same standards, whether they're new to the workspace or seasoned contributors.

**Scalable Project Knowledge** - Documentation that grows with your codebase, capturing decisions and patterns as your project evolves.

### Steering file scope

Steering files can be created with a workspace scope or a global scope.

#### Workspace steering

Workspace steering files reside in your workspace root folder under `.kiro/steering/`, and apply only to that specific workspace. Workspace steering files can be used to inform Kiro of patterns, libraries, and standards that apply to an individual workspace.

#### Global steering

Global steering files reside in your home directory under `~/.kiro/steering/`, and apply to all workspaces. Global steering files can be used to inform Kiro of conventions that apply to *all* your workspaces.

In case of conflicting instructions between global and workspace steering, Kiro will prioritize the workspace steering instructions. This allows you to specify global directives that generally apply to all your workspaces, while preserving the ability to override those directives for specific workspaces.

#### Team steering

The global steering feature can be used to define centralized steering files that apply to entire teams. Team steering files can be pushed to user's PCs via MDM solutions or Group Policies, or downloaded by users to their PCs from a central repository, and placed into the `~/.kiro/steering` folder.

### Foundational steering files

Kiro provides foundational steering files to establish core project context. You can generate these files as follows:

1. Navigate to the **Steering** section in the Kiro panel

1. Click the **Generate Steering Docs** button, or click the **+** button and select the **Foundation steering files** option

1. Kiro will create three foundational files:

**Product Overview** (`product.md`) - Defines your product's purpose, target users, key features, and business objectives. This helps Kiro understand the "why" behind technical decisions and suggest solutions aligned with your product goals.

**Technology Stack** (`tech.md`) - Documents your chosen frameworks, libraries, development tools, and technical constraints. When Kiro suggests implementations, it will prefer your established stack over alternatives.

**Project Structure** (`structure.md`) - Outlines file organization, naming conventions, import patterns, and architectural decisions. This ensures generated code fits seamlessly into your existing codebase.

These foundation files are included in every interaction by default, forming the baseline of Kiro's project understanding.

### Creating custom steering files

1. Navigate to the **Steering** section in the Kiro panel

1. Click the **+** button

1. Select the scope of the steering file: workspace or global

1. Choose a descriptive filename (e.g., `api-standards.md`)

1. Write your guidance using standard markdown syntax

1. Use natural language to describe your requirements

1. Optionally, for workspace steering files, you can use the **Refine** button to have Kiro refine your requirements

Once created, steering files become immediately available across all Kiro interactions.

### Agents.md

Kiro supports providing steering directives via the [AGENTS.md](https://agents.md/) standard. AGENTS.md files are in markdown format, similar to Kiro steering files; however, AGENTS.md files do not support [inclusion modes](#inclusion-modes) and are always included.

You can add AGENTS.md files to the global steering file location (`~/.kiro/steering/`), or to the root folder of your workspace, and they will get picked up by Kiro automatically.

### Inclusion modes

Steering files can be configured to load at different times based on your needs. This flexibility helps optimize performance and ensures relevant context is available when needed.

Configure inclusion modes by adding front matter to the top of your steering files. The front matter uses YAML syntax and must be placed at the very beginning of the file, enclosed by triple dashes (`---`).

**Info**

The inclusion configuration must be the first content in the file, no blank lines or content before it.

#### Always included (default)

```yaml
---
inclusion: always
---
```

These files are loaded into every Kiro interaction automatically. Use this mode for core standards that should influence all code generation and suggestions. Examples include your technology stack, coding conventions, and fundamental architectural principles.

**Best for**: Workspace-wide standards, technology preferences, security policies, and coding conventions that apply universally.

#### Conditional inclusion

```yaml
---
inclusion: fileMatch
fileMatchPattern: "components/**/*.tsx"
---
```

Files are automatically included only when working with files that match the specified pattern. This keeps context relevant and reduces noise by loading specialized guidance only when needed.

You can also specify multiple patterns using an array:

```yaml
---
inclusion: fileMatch
fileMatchPattern: ["**/*.ts", "**/*.tsx", "**/tsconfig.*.json"]
---
```

**Common patterns**:

- `"*.tsx"` - React components and JSX files

- `"app/api/**/*"` - API routes and backend logic

- `"**/*.test.*"` - Test files and testing utilities

- `"src/components/**/*"` - Component-specific guidelines

- `"*.md"` - Documentation files

- `["**/*.ts", "**/*.tsx"]` - All TypeScript files

- `["*.js", "*.jsx", "*.ts", "*.tsx"]` - All JavaScript and TypeScript files

**Best for**: Domain-specific standards like component patterns, API design rules, testing approaches, or deployment procedures that only apply to certain file types.

#### Manual inclusion

```yaml
---
inclusion: manual
---
```

Files are available on-demand by referencing them with `#steering-file-name` in your chat messages. This gives you precise control over when specialized context is needed without cluttering every interaction.

**Usage**: Type `#troubleshooting-guide` or `#performance-optimization` in chat to include that steering file for the current conversation. Manual steering files also appear as slash commands — type `/` in chat to see and select them.

**Best for**: Specialized workflows, troubleshooting guides, migration procedures, or context-heavy documentation that's only needed occasionally.

#### Auto inclusion

```yaml
---
inclusion: auto
name: api-design
description: REST API design patterns and conventions. Use when creating or modifying API endpoints.
---
```

Files are automatically included when your request matches the description. This works similarly to [skills](https://kiro.dev/docs/skills)—Kiro uses the description to decide when the steering file is relevant.

| Field | Required | Description |
| --- | --- | --- |
| `name` | Yes | Identifier for the steering file. Used for display and matching. |
| `description` | Yes | When to include this file. Kiro matches this against your requests. |

Auto-inclusion steering files also appear as slash commands in chat. Type `/` followed by the steering file name to explicitly include it, in addition to the automatic activation based on description matching.

**Best for**: Context-heavy guidance that should only load when relevant—like specialized domain knowledge, complex workflows, or detailed reference material that would overwhelm always-on steering.

### File references

Link to live workspace files to keep steering current:

```markdown
#[[file:<relative_file_name>]]
```

Examples:

- API specs: `#[[file:api/openapi.yaml]]`

- Component patterns: `#[[file:components/ui/button.tsx]]`

- Config templates: `#[[file:.env.example]]`

### Best practices

**Keep Files Focused**
One domain per file - API design, testing, or deployment procedures.

**Use Clear Names**

- `api-rest-conventions.md` - REST API standards

- `testing-unit-patterns.md` - Unit testing approaches

- `components-form-validation.md` - Form component standards

**Include Context**
Explain why decisions were made, not just what the standards are.

**Provide Examples**
Use code snippets and before/after comparisons to demonstrate standards.

**Security First**
Never include API keys, passwords, or sensitive data. Steering files are part of your codebase.

**Maintain Regularly**

- Review during sprint planning and architecture changes

- Test file references after restructuring

- Treat steering changes like code changes - require reviews

### Common steering file strategies

**API Standards** (`api-standards.md`) - Define REST conventions, error response formats, authentication flows, and versioning strategies. Include endpoint naming patterns, HTTP status code usage, and request/response examples.

**Testing Approach** (`testing-standards.md`) - Establish unit test patterns, integration test strategies, mocking approaches, and coverage expectations. Document preferred testing libraries, assertion styles, and test file organization.

**Code Style** (`code-conventions.md`) - Specify naming patterns, file organization, import ordering, and architectural decisions. Include examples of preferred code structures, component patterns, and anti-patterns to avoid.

**Security Guidelines** (`security-policies.md`) - Document authentication requirements, data validation rules, input sanitization standards, and vulnerability prevention measures. Include secure coding practices specific to your application.

**Deployment Process** (`deployment-workflow.md`) - Outline build procedures, environment configurations, deployment steps, and rollback strategies. Include CI/CD pipeline details and environment-specific requirements.

### Related documentation

- [Skills](https://kiro.dev/docs/skills) - On-demand modular instruction packages for specialized workflows

- [Hooks](https://kiro.dev/docs/hooks) - Automate agent actions based on events

Page updated:  February 18, 2026[Switching agents](https://kiro.dev/docs/custom-agents/agent-selector/)[Agent Skills](https://kiro.dev/docs/skills/)

---

# Spec-Driven Development

### What are specs?

Specs or specifications are structured artifacts that formalize the development process for features and bug fixes in your application. They provide a systematic approach to transform high-level ideas into detailed implementation plans with clear tracking and accountability.

With Kiro's specs, you can:

- **Break down requirements** into user stories with acceptance criteria

- **Build design docs** with sequence diagrams and architecture plans

- **Track implementation progress** across discrete tasks

- **Collaborate effectively** between product and engineering teams

### Core Structure

Every spec generates three key files that form the foundation of your specification:

- **requirements.md** (or **bugfix.md**) - Captures user stories, acceptance criteria, or bug analysis in structured notation

- **design.md** - Documents technical architecture, sequence diagrams, and implementation considerations

- **tasks.md** - Provides a detailed implementation plan with discrete, trackable tasks

$!Loading diagram.../$

### Three-Phase Workflow

All specs follow a three-phase workflow that transforms your idea into executable implementation:

**Requirements or Bug Analysis** - Define what needs to be built or fixed

- Feature Specs: User stories and acceptance criteria in `requirements.md`

- Bugfix Specs: Bug analysis with current/expected/unchanged behavior in `bugfix.md`

**Design** - Create technical architecture and implementation approach in `design.md`

- System architecture and component design

- Sequence diagrams and data flow

- Error handling and testing strategy

**Tasks** - Generate discrete, executable implementation tasks in `tasks.md`

- Trackable tasks with clear outcomes

- Real-time status updates as you implement

- Run tasks individually or all at once

### Task Execution

Kiro provides a task execution interface for `tasks.md` files that displays real-time status updates. Tasks are updated as in-progress or completed, allowing you to efficiently track implementation progress and maintain an up-to-date view of your development status.

#### Running tasks in parallel

When you click **Run all Tasks** on a spec, Kiro analyzes your task list, figures out which tasks depend on each other, and runs independent tasks concurrently. For most feature specs, this cuts execution time significantly without any setup.

Kiro builds a **dependency graph** of the tasks in your `tasks.md` and groups independent tasks into **waves**:

- **Wave 1** — all tasks with no dependencies. These run concurrently.

- **Wave 2** — all tasks whose dependencies were satisfied by Wave 1. These run concurrently.

- **Wave N** — continues until all tasks are complete.

Waves execute sequentially; tasks within a wave execute concurrently.



### Types of Specs

Kiro supports two types of specs to match your development needs:

#### Feature Specs

For building new features and capabilities in your application. Feature Specs guide you through requirements gathering, technical design, and implementation planning with two workflow variants: Requirements-First and Design-First. For well-understood features, you can also use [Quick Plan](https://kiro.dev/docs/specs/quick-plan) to auto-generate all three artifacts without approval gates.

[Learn more about Feature Specs →](https://kiro.dev/docs/specs/feature-specs)

#### Bugfix Specs

For systematically diagnosing and fixing bugs with surgical precision while preventing regressions. Bugfix Specs help you identify root causes, design fixes, and validate that nothing else breaks.

[Learn more about Bugfix Specs →](https://kiro.dev/docs/specs/bugfix-specs)

### Getting Started

Ready to create your first Spec? Here's how:

1. From the Kiro pane, click the `+` button under **Specs**. Alternatively, choose **Spec** from the chat pane.

1. Kiro will ask if you are developing a Feature or fixing a Bug


    - If you choose Feature, describe your feature and choose your workflow: **Requirements-First** or **Design-First**

    - If you choose Bug, describe your bug

1. Follow the workflow through each phase to implementation

### When to Use Specs vs Vibe

**Use Specs when:**

- Building complex features requiring structured planning

- Fixing bugs where regressions are costly

- You need documentation for team collaboration

- Requirements or design need iteration

**Use Vibe when:**

- Quick exploratory coding

- Prototyping without clear goals

### Learn more

Dive deeper into Kiro's Spec system with these guides:

[Feature SpecsBuild new features with structured workflows.](https://kiro.dev/docs/specs/feature-specs/)[Quick PlanGenerate requirements, design, and tasks in one pass without approval gates.](https://kiro.dev/docs/specs/quick-plan/)[Analyze RequirementsCatch inconsistencies, ambiguities, and gaps in your requirements before design.](https://kiro.dev/docs/specs/analyze-requirements/)[Bugfix SpecsFix bugs surgically while preventing regressions.](https://kiro.dev/docs/specs/bugfix-specs/)[Best PracticesFAQs on best practices when working with specs.](https://kiro.dev/docs/specs/best-practices/)Page updated:  June 25, 2026[Extension registry](https://kiro.dev/docs/editor/extension-registry/)[Feature Specs](https://kiro.dev/docs/specs/feature-specs/)

---

# Agent Hooks

Agent hooks are automated triggers that execute agent prompts or shell commands when specific events occur in your IDE. Rather than manually asking for routine tasks, hooks handle them automatically.

### What are agent hooks?

Agent hooks set up automated responses to events such as:

- Saving, creating, or deleting files

- User prompt submission and agent turn completion

- Before or after tool invocations

- Before or after spec task execution

By setting up hooks for common tasks, you can:

- Maintain consistent code quality

- Prevent security vulnerabilities

- Reduce manual overhead

- Standardize team processes

### How agent hooks work

The agent hook system follows a two-step process:

1. **Event Detection**: The system monitors for specific events in your IDE

1. **Automated Action**: When an event occurs, an action (either an agent prompt or a shell command) is executed

### Setting up agent hooks

**Info**

IDE 1.0 changes the UI for creating hooks. See [What's new in IDE 1.0](https://kiro.dev/docs/whats-new-1-0#hooks) for the updated flow and migration steps.

You can create hooks in three ways: describe what you want in natural language, manually fill out a form, or write a JSON file directly.

#### JSON file format

Hooks are JSON files stored in `.kiro/hooks/` at the workspace level:

```json
{
  "version": "v1",
  "hooks": [
    {
      "name": "lint-on-save",
      "trigger": "PostFileSave",
      "matcher": "\\.ts$",
      "action": { "type": "command", "command": "npm run lint" },
      "timeout": 30,
      "enabled": true
    }
  ]
}
```

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | string | Yes |  | Identifier shown in telemetry |
| `description` | string | No |  | Documentation only |
| `trigger` | string | Yes |  | When the hook fires |
| `matcher` | regex string | No | always-match | Filters by tool name or file path |
| `action` | object | Yes |  | `{ type: "command", command: "..." }` or `{ type: "agent", prompt: "..." }` |
| `timeout` | integer (seconds) | No | 60 | 0 disables timeout. Ignored for agent actions |
| `enabled` | boolean | No | true | Set false to skip without deleting |

#### Creating a hook from the UI

1. Navigate to the **Agent Hooks** section in the Kiro panel

1. Click the **+** button to create a new hook

1. Choose how you want to create the hook:


    - **Manually create a hook** — configure a hook by hand in a form

    - **Ask Kiro to create a hook** — describe a hook using natural language and have Kiro create one

#### Ask Kiro to create a hook

1. Select **Ask Kiro to create a hook**

1. Describe the hook workflow using natural language

1. Press **Enter** or click **Submit** to proceed

1. Review the generated configuration, adjust if needed, and click **Save Hook**

#### Manually create a hook

1. Select **Manually create a hook** to open the hook form

1. Fill in the form fields:


    - **Title** — a short name for the hook

    - **Description** — what the hook does

    - **Event** — the trigger type (e.g., File Save, Post Tool Use, Pre Task Execution)

    - **Tool name** — for Pre/Post Tool Use hooks, specify which tools to match

    - **File pattern** — for file event hooks, specify which files to match

    - **Action** — choose **Ask Kiro** (agent prompt) or **Run Command** (shell command)

    - **Instructions** or **Command** — the prompt or shell command to execute

1. Click **Create Hook** when done, or **Clear** to reset the form

You can also open the Hook UI from the Command Palette with `Cmd + Shift + P` (Mac) or `Ctrl + Shift + P` (Windows/Linux) and typing `Kiro: Open Kiro Hook UI`.

### Trigger reference

| Trigger | Fires when | Matcher matches | Can block? |
| --- | --- | --- | --- |
| `SessionStart` | Session begins |  | No |
| `Stop` | Agent completes its turn |  | No |
| `PreToolUse` | Before tool executes | Tool name (regex) | Yes |
| `PostToolUse` | After tool executes | Tool name (regex) | No |
| `PreTaskExec` | Before a spec task starts |  | Yes |
| `PostTaskExec` | After a spec task finishes |  | No |
| `UserPromptSubmit` | User submits a prompt |  | Yes |
| `PostFileCreate` | After a file is created by the agent | File path (regex) | No |
| `PostFileSave` | After a file is saved by the agent | File path (regex) | No |
| `PostFileDelete` | After a file is deleted by the agent | File path (regex) | No |

**Info**

Manual hooks have been replaced by manual steering files. See [Steering](https://kiro.dev/docs/steering) for details.

### Exit code behavior

For command actions:

| Exit code | Behavior |
| --- | --- |
| `0` | Success. STDOUT added to context (SessionStart, UserPromptSubmit) or ignored (others) |
| `2` | Block execution (PreToolUse, UserPromptSubmit, PreTaskExec only). STDERR returned to the agent |
| Other | Warning shown to user. Tool execution proceeds |

### Next steps

Now that you have created a hook file, you can further learn about hooks here:

- **[Hook Types](https://kiro.dev/docs/hooks/types)** - Learn about different trigger types and their use cases

- **[Hook Actions](https://kiro.dev/docs/hooks/actions)** - Learn about different hook actions and their use cases

- **[Management](https://kiro.dev/docs/hooks/management)** - Learn how to organize, edit, and maintain your hooks

- **[Best Practices](https://kiro.dev/docs/hooks/best-practices)** - Follow patterns for effective hook design

- **[Examples](https://kiro.dev/docs/hooks/examples)** - See examples and templates you can use

Page updated:  July 9, 2026[Create powers](https://kiro.dev/docs/powers/create/)[Hook triggers](https://kiro.dev/docs/hooks/types/)

---

# Model Context Protocol (MCP)

Model Context Protocol (MCP) extends Kiro's capabilities by connecting to specialized servers that provide additional tools and context. This guide helps you set up, configure, and use MCP servers with Kiro.

### What is MCP?

MCP is a protocol that allows Kiro to communicate with external servers to access specialized tools, prompts, and resources. For example, the AWS Documentation MCP server provides tools to search, read, and get recommendations from AWS documentation directly within Kiro.

With MCP, you can:

- Access specialized knowledge bases and documentation

- Integrate with external services and APIs

- Extend Kiro's capabilities with domain-specific tools

- Use server-provided prompt templates and resource templates via the `#` mention system in chat

- Respond to server elicitation requests when tools need additional input during execution

- Create custom tools for your specific workflows

### Setting up MCP

#### Prerequisites

Before using MCP, make sure you have:

1. The latest version of Kiro installed

1. Any specific prerequisites for the MCP servers you want to use (listed in each server's documentation)

### Managing MCP servers

#### Enabling MCP support

After creating your configuration file:

1. Open Settings with `Cmd + ,` (Mac) or `Ctrl + ,` (Windows/Linux)

1. Search for "MCP"

1. Enable the MCP support setting

#### Using the MCP servers tab

The Kiro panel includes an MCP servers tab that shows:

- All configured MCP servers

- Connection status indicators

- Quick access to server tools

To use this feature:

1. Select the Kiro icon in the activity bar

1. Navigate to the MCP servers tab

1. Click any tool name to insert a placeholder prompt in the chat

### Troubleshooting

If you encounter issues with MCP servers:

#### Checking MCP logs

1. Open the Kiro panel

1. Select the Output tab

1. Choose "Kiro - MCP Logs" from the dropdown

#### Common issues and solutions

| Issue | Solution |
| --- | --- |
| Connection failures | Verify prerequisites are installed correctly |
| Permission errors | Check that tokens and API keys are valid |
| Tool not responding | Review MCP logs for specific error messages |
| Configuration not loading | Validate JSON syntax and save the config file |

### Additional resources

- [Official MCP Documentation](https://modelcontextprotocol.io/introduction)

### Next steps

Now that you have created a MCP server, you can further learn about MCP servers here:

- **[Configuring MCPs](https://kiro.dev/docs/mcp/configuration/)** - Learn about configuring Model Context Protocol (MCP) servers

- **[MCP Server management](https://kiro.dev/docs/mcp/servers/)** - Learn how to use common MCP servers with examples

- **[Using MCP Tools](https://kiro.dev/docs/mcp/usage/)** - Learn how to effectively use MCP tools with Kiro

- **[Best Practices](https://kiro.dev/docs/mcp/security/)** - Best practices for effective MCP usage

Page updated:  February 18, 2026[Agent Skills](https://kiro.dev/docs/skills/)[Configuration](https://kiro.dev/docs/mcp/configuration/)

---

# Command Line Interface (CLI)

The Kiro CLI brings the power of AI-assisted development to your terminal. Build, test, and deploy applications using natural language commands and automated workflows.

Get started with the Kiro CLI in minutes.

Install on   macOS, Linux, or  Windows`curl -fsSL https://cli.kiro.dev/install | bash`

Start using Kiro CLI:

```bash
cd my-project
kiro-cli
```

### Core features

[Interactive ChatEngage with Kiro through natural conversation in your terminal.](https://kiro.dev/docs/cli/chat/)[Custom AgentsCreate and deploy specialized agents for your workflows.](https://kiro.dev/docs/cli/custom-agents/)[MCP IntegrationConnect external tools and data sources through Model Context Protocol.](https://kiro.dev/docs/cli/mcp/)[Smart HooksAutomate workflows with intelligent pre/post command hooks.](https://kiro.dev/docs/cli/hooks/)[Agent SteeringSteer Kiro agent with your best practices and preferences.](https://kiro.dev/docs/cli/steering/)[Auto CompleteIntelligent command completion with context awareness.](https://kiro.dev/docs/cli/autocomplete/)

### Use cases

The Kiro CLI is perfect for:

- **Interactive Development**: Chat with Kiro directly in your terminal for instant help

- **Custom Automation**: Create specialized agents for your specific workflows

- **Team Standardization**: Use team-level best practices and preferences

- **External Integrations**: Connect tools and services through MCP servers

- **Intelligent Assistance**: Get context-aware suggestions and auto-completion

- **Headless Automation**: Run prompts non-interactively in CI/CD pipelines using [API key authentication](https://kiro.dev/docs/cli/headless)

- **Workflow Optimization**: Automate repetitive tasks with smart hooks

Page updated:  April 19, 2026[Quick start](https://kiro.dev/docs/cli/quick-start/)

---

# Web Interface

**Preview**Kiro on the web is currently in preview for Kiro Pro, Pro+, Pro Max, and Power users. Available in the US region only during the preview. Features and documentation may change as we improve the product.

Kiro Web (Preview) is a browser-based development agent that helps you build software through conversation. Chat with the agent to discuss approaches, write code, and open pull requests — all from [app.kiro.dev](https://app.kiro.dev).

Kiro Web works in two modes. By default, you collaborate with the agent interactively — iterating on a problem together and asking it to open a pull request when you're ready. When you need the agent to own the outcome end-to-end, toggle on [autonomous mode](https://kiro.dev/docs/web/autonomous-mode) and let it plan, implement, and open a PR on its own.

### Prerequisites

- A paid Kiro subscription (Pro or higher)

- A [GitHub account connected](https://kiro.dev/docs/web/github) to Kiro

### AWS Identity Center

If your organization uses AWS Identity Center, your administrator must first enable Kiro Web from **Settings > Kiro Settings** in the AWS account where Kiro is configured. Kiro Web is available in **US East (N. Virginia) `us-east-1`** only during the preview. See the [Identity Center setup guide](https://kiro.dev/docs/web/identity-center) for additional requirements.

### Get started

[SetupConnect GitHub and configure access](https://kiro.dev/docs/web/setup/)[Working with the agentChat, iterate, and open pull requests](https://kiro.dev/docs/web/using-the-agent/)

### Features

[SpecsPlan features, bugs, and quick plans — then have the agent implement and open a PR](https://kiro.dev/docs/web/specs/)[Autonomous modeLet the agent own the outcome — it plans, codes, and opens PRs](https://kiro.dev/docs/web/autonomous-mode/)[AutomationsSchedule recurring tasks on a cron — Kiro runs and opens PRs automatically](https://kiro.dev/docs/web/automations/)[SteeringGuide the agent with your team's standards and conventions](https://kiro.dev/docs/web/steering/)[SandboxIsolated execution environment with configurable access controls](https://kiro.dev/docs/web/sandbox/)[GitHub integrationRepositories, branches, pull requests, and issue-based tasks](https://kiro.dev/docs/web/github/)[GitLab integrationAdd a GitLab project, work on it, and open a merge request](https://kiro.dev/docs/web/gitlab/)Page updated:  June 18, 2026[Setup](https://kiro.dev/docs/web/setup/)

---

# Learn by Playing

In this guide, you will learn how to use Kiro by completing tasks
in the [codebase](https://github.com/kirodotdev/spirit-of-kiro) for a sample video game called Spirit of Kiro.

95% of the code for Spirit of Kiro has been written by prompting Kiro.
You are going to be using Kiro to fix bugs and add features to the game to
complete it.

Loading image...![A cartoon ghost stands in front of a large industrial lever labeled "PULL"
and a workbench with tools. The ghost is next to a glowing card and a prompt
showing the "E" key.](https://kiro.dev/images/video-game-guide/intro.png?h=4e4c1049)

Spirit of Kiro is an infinite crafting game in which you can:

1. Discover unique, randomly generated objects

1. Utilize these items on each other via simulated interactions like "cut",
    "paint", "glue", "enchant". Item's combine, break apart, and change in
    response to these interactions.

1. Sell your resulting creations to an AI appraiser.

Every object in the game is generated by AI. Interactions between objects
are also simulated by AI. This gives Spirit of Kiro infinite replayability
and potential.

In the following diagram you can see how the game's core crafting mechanic works. The
player has discovered two items: a spoon, and a glass jar of vegetables. The player
can use the spoon to extract a sample of the vegetables.

Loading image...![A crafting workbench interface from a game, showing a grid of unique items
and pop-up descriptions for items like a botanical extraction spoon, and jar of vegetables,
Purple arrows connect the workbench to detailed item info
panels, with the text 'Discover Unique Items' and 'Add items to workbench',
and "Freeform crafting outcomes" above.](https://kiro.dev/images/video-game-guide/crafting.png?h=e11442f7)

While the game’s core loop is complete, the game is not quite done yet. There is an
[extensive roadmap for the game](https://github.com/kirodotdev/spirit-of-kiro/blob/main/docs/ROADMAP.md),
full of additional ideas to build, and there a few bugs that have been left in the
game on purpose so you can try out solving them using Kiro.

In this guide you will learn to use Kiro by completing a series of tasks
on a `challenge` branch of the open source code for this game. Ready to get started?
Let's go!

1

##### Setup

First, we ensure that you have an AWS account. We setup a Cognito user
pool for authentication, build and launch the game stack using a
Docker Compose file, then bootstrap DynamoDB tables. Then we verify
that the game runs on your local machine:

- [Setup dev environment and launch the game](./00-setup)

2

##### Task: Improve game homepage

We setup steering files to help Kiro understand the project.
With a full understanding of the project, we put Kiro to
work improving the home landing page for the game.

- [Steering Kiro, and improving the game homepage](./01-improve-the-homepage)

3

##### Bug Fix: Physics Glitch

When we tab out of game, the physics goes haywire when tabbing
back in. Can Kiro fix it?

- [Investigating and fixing a subtle bug with physics](./02-physics-bug)

4

##### Bug Fix: Interactions Oversight

The original pass at game interactions was "vibe coded".
But it looks like AI missed something. Can Kiro correct its own mistake?

- [Fixing a complex issue across multiple files](./03-interactions-bug)

5

##### Refactor: DRY up code with Kiro

It's not just vibe coding, we do vibe refactoring here as well.

- [Vibe refactoring is 50% of vibe coding](./04-dry-code-refactor)

6

##### New Feature: Implementing something complex

The game is currently missing email verification and password reset.
We implement this relatively complex new feature across client and server.

- [Using specifications for complex work](./05-using-specs-for-complex-work)

7

##### Automation: Managing assets with agent hooks

We identify some boilerplate asset management work that that is error prone.
Fortunately Kiro agent hooks can help us automate this.

- [Managing assets with agent hooks](./06-managing-assets-with-agent-hooks)

8

##### Extending Kiro with MCP

Not only can you make this game your own, you can also make Kiro your own,
by extending its context and behaviors with Model Context Protocol (MCP).

- [Extending Kiro with MCP](./07-extending-kiro-with-mcp)

9

##### Conclusion

Wrap up your learning journey and explore next steps.

- [Conclusion](./99-conclusion)

Page updated:  November 18, 2025[Java](https://kiro.dev/docs/guides/languages-and-frameworks/java-guide/)[Setup dev environment and launch the game](https://kiro.dev/docs/guides/learn-by-playing/00-setup/)

---

# Privacy & Security

Kiro is an AWS application that works as a standalone agentic IDE. Kiro's security framework is built around AWS's security infrastructure and follows practices to protect your development environment and data. Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud:

- Security of the cloud – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Kiro, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).

- Security in the cloud – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations

This documentation helps you understand how to apply the shared responsibility model when using Kiro. It shows you how to configure Kiro to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Kiro resources.

### URL fetching

In the Kiro chat module, you can paste a specific URL for your device to fetch and use it as context to help Kiro answer your query or solve your task. You are responsible for the URL content that you fetch and ensuring that your use complies with any applicable third-party terms and laws.

### Autopilot versus supervised mode

Kiro offers two interaction modes, Autopilot and Supervised, that control how you review agent actions. Both modes grant the agent the same capabilities: creating, modifying, searching, and deleting files in your codebase and running commands that impact the filesystem. The difference is the review workflow, not the underlying permissions or access scope.

**Warning**

**Supervised mode is a code review workflow, not a security control.** It is designed to help you review and approve agent-generated changes. It does not function as a sandbox, isolation boundary, or access control mechanism. To restrict what the agent can access or modify, use [protected paths](#protected-paths), [trusted commands](#trusted-commands), workspace isolation, and credential scoping as described in [best practices](#best-practices).

| Capability | Autopilot | Supervised |
| --- | --- | --- |
| Agent can read files | Yes | Yes |
| Agent can write files to disk | Yes | Yes |
| Agent can run commands | Yes (with trusted commands policy) | Yes (with trusted commands policy) |
| Review step before changes are applied | No, changes are applied immediately | Yes, you review a diff and accept or reject |
| Revert capability | Manual (via **Revert all changes** or checkpoints) | Automatic on rejection; also manual revert available |
| Prevents writes to protected paths without approval | Yes | Yes |

#### How supervised mode works

In both modes, the agent writes file changes to disk during tool execution. In supervised mode, these writes are tagged for your review. After the agent's turn completes, Kiro checks for pending file changes and prompts you to accept or reject before continuing. If you reject, files revert to their pre-turn state.

Kiro classifies the following operations as file-modifying. Any of these operations triggers a mandatory review prompt at the end of the agent's turn:

| Operation | Description |
| --- | --- |
| File creation or overwrite | Creating new files or replacing file contents |
| Text replacement | Replacing specific text within a file |
| Content append | Adding content to the end of a file |
| File deletion | Removing a file from the workspace |
| Code editing | Modifying code within a file |
| Symbol rename | Renaming a variable, function, or class across files |
| File relocation | Moving a file and updating its references |

This review check is built into Kiro's workflow and cannot be skipped by the AI model. If a file-modifying operation ran during the turn, the approval prompt will appear.

Shell commands follow a separate approval path. By default, all commands require your approval before execution (see [trusted commands](#trusted-commands)). To maintain full oversight, keep your trusted commands list minimal and avoid broad wildcards.

#### What supervised mode provides

When supervised mode is enabled, Kiro enforces the following behaviors for file-modifying operations:

- **Turn-level review for file-modifying operations:** Every file-modifying operation listed above results in an approval prompt before changes are applied.

- **Automatic revert on rejection:** If you reject, files are restored to their exact state before the agent's turn began.

- **Protected path enforcement:** Writes to [protected paths](#protected-paths) require explicit approval before the write occurs, in both modes.

- **Command approval:** Unrecognized commands require your approval before execution, in both modes.

#### Scope and limitations

Supervised mode reviews changes made through Kiro's file-editing operations. Other actions, such as shell commands you've added to your trusted list, follow their own approval policy. Supervised mode does not restrict which files the agent can read, which commands it can suggest, or what network access it has.

To maintain full oversight of your environment:

- Keep your [trusted commands](#trusted-commands) list minimal and avoid broad wildcards.

- Use [protected paths](#protected-paths) to require approval for writes to sensitive locations.

- Use workspace isolation and credential scoping as described in [best practices](#best-practices).

#### Autopilot mode (default)

In Autopilot mode, Kiro works autonomously:

- Kiro executes multiple steps without requiring approval for each one.

- Kiro makes decisions based on its understanding of your requirements.

- You can toggle autopilot on/off in the chat interface.

- Changes are written and applied immediately. You can review them after the fact.

- You can interrupt at any time and revert changes via **Revert all changes** or [checkpoints](https://kiro.dev/docs/chat/checkpoints).

#### Supervised mode

In Supervised mode, Kiro works interactively, pausing for your review after each turn:

- After the agent modifies files, it pauses and presents a diff for your review.

- You can accept individual changes (hunk-level granularity) or reject them to revert.

- The agent asks clarifying questions when needed.

- To reduce interruptions, consecutive edits to the same file may be batched.

Supervised mode is best suited for situations where you want to closely review agent output. For example, when working in an unfamiliar codebase, making changes to critical paths, or onboarding a new team member to agent-assisted workflows.

#### Choosing the right mode

Use **Autopilot** when you trust the task scope and want the agent to work efficiently without interruption. Use **Supervised** when you want to review each set of changes before they persist. In both cases, apply the security controls described in [best practices](#best-practices) to protect sensitive files, credentials, and infrastructure.

When operating in either mode, you can view individual or all file changes made by the agent by selecting **View all changes** in the **Chat** module. You can also select **Revert all changes** or revert to a [checkpoint](https://kiro.dev/docs/chat/checkpoints) to restore your files to their previous state.

### Trusted commands

By default, Kiro requires approval before running any command. You can create your own trusted commands list by searching for **Kiro Agent: Trusted Commands** in your settings.

Kiro uses simple string prefix matching to determine if a command should be automatically trusted:

- **Exact matching**: Commands must match exactly (e.g., `npm install`)

- **Wildcard matching**: Use `*` to trust command variations (e.g., `npm *` trusts all npm commands)

- **Universal trust**: Use `*` alone to trust all commands (use with extreme caution)

The system treats entire commands as single strings and only checks if they start with trusted patterns. It does not analyze command structure, chains, or special characters, putting full responsibility on you to carefully configure trusted patterns.

### Protected paths

Kiro requires explicit approval before writing to certain protected paths, preventing unintended modifications to sensitive workspace configuration files. This applies in both Autopilot and Supervised mode — when the agent attempts to create or modify a file matching a protected pattern, you see a confirmation prompt and the change is not applied until you approve it. If you decline, the agent skips the write and continues with the rest of the task.

#### Protected path patterns

The following path patterns are protected:

| Pattern | Match type | Description |
| --- | --- | --- |
| `.vscode/` | Path contains | VS Code workspace settings |
| `vscode~` | Path contains | VS Code backup and recovery files |
| `.git/` | Path contains | Files inside the `.git` directory |
| `git~` | Path contains | Git lock and backup files |
| `.code-workspace` | Path contains | Multi-root workspace files |
| `.git` | Exact basename | The `.git` directory or submodule file itself |
| `mcp.json` | Exact basename | MCP server configuration |
| `.kiroignore` | Exact basename | Kiro ignore rules |

#### Match types

- **Path contains** — Matches if the pattern appears anywhere in the file path. For example, `.vscode/` matches both `.vscode/settings.json` and `.vscode/extensions.json`.

- **Exact basename** — Matches if the filename (the last segment of the path) exactly equals the pattern. For example, `mcp.json` matches `project/mcp.json` but not `mcp.json.bak`.

When a match is detected, Kiro pauses and displays a confirmation prompt. The file is not written until you approve.

### Best practices

Kiro provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

#### Protecting your resources

When using GitHub or Google authentication with Kiro, be aware that the Kiro agent operates within your local environment and may access:

- Local files and repositories

- Environment variables

- AWS credentials stored in your environment

- Other configuration files with sensitive information

#### Recommendations

1. **Workspace Isolation**


    - Keep sensitive projects in separate workspaces

    - Use .gitignore to prevent access to sensitive files

    - Consider using workspace trust features in your IDE

1. **Use a Clean Environment**


    - Consider creating a dedicated user account or container environment for Kiro

    - Limit access to only the repositories and resources needed for your current project

1. **Manage AWS Credentials Carefully**


    - Use temporary credentials with appropriate permissions

    - Consider using AWS named profiles to isolate Kiro's access

    - For sensitive work, remove AWS credentials from your environment when not needed

1. **Repository Access Control**


    - When using GitHub authentication, review which repositories Kiro can access

    - Use repository-specific access tokens when possible

    - Regularly audit access permissions

### Remote extensions security

**Warning**

**Security Note**: Using remote extensions opens a connection between your local machine and the remote machine. Only connect to secure remote machines that you trust and that are owned by a party whom you trust. A compromised remote could use the connection to execute code on your local machine.
Third-party extensions including remote extensions are not developed, maintained, or managed by Kiro. We are not responsible for third-party extensions and cannot guarantee their stability, compatibility, or ongoing support.

Kiro supports Open VSX extensions, including remote SSH extensions (the community-maintained [Open Remote - SSH](https://open-vsx.org/extension/jeanp413/open-remote-ssh) extension on Open VSX is a popular choice), to provide a familiar development experience. For comprehensive information about extension compatibility and support in Kiro, see our [extension compatibility guide](https://kiro.dev/docs/guides/migrating-from-vscode/#extension-compatibility).

By following these practices, you can enjoy Kiro's capabilities while maintaining appropriate security boundaries for your development environment.

Page updated:  May 15, 2026[Agent Focus Mode](https://kiro.dev/docs/experimental/focus-mode/)[Data protection](https://kiro.dev/docs/privacy-and-security/data-protection/)
