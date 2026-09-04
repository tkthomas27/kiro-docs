# Kiro IDE Comprehensive Documentation
*Compiled on September 04, 2026*

---
# Get Started

Kiro is an AI-powered development environment that helps you build software from prototype to production. One [unified agent harness](https://kiro.dev/docs/how-kiro-works/) powers every surface (IDE, CLI, Web, and Mobile) so your configuration, specs, and steering work everywhere.

[IDE](https://kiro.dev/docs/ide/)Loading image...![Kiro in the browser interface](https://kiro.dev/images/home/primary-web.png?h=f855b545)[Web](https://kiro.dev/docs/web/)

Terminal — 80×24

Loading cast file...[CLI](https://kiro.dev/docs/cli/)Loading image...![Kiro iOS interface](https://kiro.dev/images/home/ios.png?h=ced0921c)[Mobile](https://kiro.dev/docs/mobile/)

### Choose your surface

Pick the surface that fits your workflow. Your `.kiro/` configuration is shared across all of them.

[IDEDesktop editor with chat, specs, hooks, and full editor integration](https://kiro.dev/docs/ide/)[CLITerminal-native agent with headless mode, session management, and CI integration](https://kiro.dev/docs/cli/)[WebBrowser-based agent for multi-repo tasks that plans, implements, and opens PRs](https://kiro.dev/docs/web/)[MobileMonitor tasks, review PRs, and chat with your agent on the go](https://kiro.dev/docs/mobile/)[CrewPersonal AI agent with autonomous tasks, scheduling, memory, and multi-channel access](https://kiro.dev/docs/crew/)

### What you can do

| I want to... | Use |
| --- | --- |
| Plan a feature with requirements, design, and tasks | [Specs](https://kiro.dev/docs/specs/) |
| Fix a bug with root cause analysis and regression prevention | [Bugfix Specs](https://kiro.dev/docs/specs/bugfix-specs/) |
| Chat and build iteratively without a plan | [Chat](https://kiro.dev/docs/ide/chat/) (IDE) or start a session (CLI) |
| Enforce project standards automatically | [Steering](https://kiro.dev/docs/steering/) |
| Automate actions on agent file changes, tool use, or task completion | [Hooks](https://kiro.dev/docs/hooks/) |
| Connect external tools and APIs | [MCP](https://kiro.dev/docs/mcp/) |
| Control what the agent can access | [Permissions](https://kiro.dev/docs/permissions/) |
| Create specialized agents for specific workflows | [Custom agents](https://kiro.dev/docs/custom-agents/) |
| Extend the agent with reusable instruction packages | [Skills](https://kiro.dev/docs/skills/) |
| Add tools with built-in knowledge that activate on demand | [Powers](https://kiro.dev/docs/powers/) |
| Delegate parallel tasks to focused sub-agents | [Sub-agents](https://kiro.dev/docs/custom-agents/subagents/) |
| Undo agent changes or fork a conversation | [Checkpoints and rewind](https://kiro.dev/docs/checkpoints/) |
| Keep secrets and sensitive files away from the agent | [Kiroignore](https://kiro.dev/docs/kiroignore/) |
| Keep long sessions productive within context limits | [Compaction](https://kiro.dev/docs/compaction/) |

### Get started

[Install KiroSet up the IDE, CLI, or Web in under 5 minutes](https://kiro.dev/docs/getting-started/installation/)[Your first projectWalk through specs, steering, and hooks hands-on](https://kiro.dev/docs/getting-started/first-project/)

### One agent, every surface

Every Kiro surface is a front end to the same unified agent harness. Shared project configuration travels with your repository through `.kiro/`, with surface-specific behavior for permissions and primary-agent selection. Start a spec in the IDE, continue it from the CLI, hand off implementation to the Web agent, and keep the same project context across surfaces.

Each surface adds its own way of working on top: the IDE brings editor integration, the CLI brings terminal-native and headless workflows, and the Web brings zero-setup sandboxed sessions. [How Kiro works](https://kiro.dev/docs/how-kiro-works/) explains the architecture, the agent loop, and where every capability plugs in.

### Learn more

[Interactive tutorialBuild a real project while learning Kiro's features through a game-based walkthrough](https://kiro.dev/docs/guides/learn-by-playing/)[ModelsAvailable AI models and how to select them](https://kiro.dev/docs/models/)[Privacy and securityHow Kiro handles your code and data](https://kiro.dev/docs/privacy-and-security/)[EnterpriseSSO, governance, usage monitoring, and team management](https://kiro.dev/docs/enterprise/concepts/)Page updated:   September 2, 2026[Installation](https://kiro.dev/docs/getting-started/installation/)

---

# Installation

Kiro is available as a desktop IDE, a command-line interface, a web app, a mobile app, and a personal AI agent (Crew). Pick the surface that fits your workflow. You can use more than one, and your `.kiro` configuration is shared across all of them.

### System requirements

**IDE** - macOS (Intel + Apple Silicon), Windows 10/11 (64-bit), or Linux (Ubuntu 24+, Debian 13+, Fedora 40+, Arch, Mint 22+).

**CLI** - macOS, Windows 11 (PowerShell), or Linux (glibc 2.34+ or musl variant).

**Web** - Any modern browser. No local installation required.

**Mobile** - iOS, distributed through Apple TestFlight during early access.

**Crew** - macOS, Linux (x86_64 and ARM), or Windows. Python 3.9+ required for source installs.

### Install Kiro

IDECLIWebMobileCrew1

##### Download Kiro

Go to [kiro.dev](https://kiro.dev) and download the installer for your operating system (macOS, Windows, or Linux).

2

##### Run the installer

Open the downloaded file and follow the installation instructions for your platform.

3

##### Sign in

When you open Kiro for the first time, sign in with a provider of your choice (Google, GitHub, AWS Builder ID, or organization identity). Learn more about [authentication](https://kiro.dev/docs/getting-started/authentication/).

4

##### Import settings (optional)

You can [import your VS Code settings and extensions](https://kiro.dev/docs/upgrade-guides/migrating-from-vscode/). If you use another editor, skip this step and select your preferred theme.

5

##### Open a project

From the welcome page, open a folder to start your first session. See [Your first project](https://kiro.dev/docs/getting-started/first-project/) for a guided walkthrough.

### Upgrading

IDECLIWeb

Kiro IDE downloads updates automatically in the background. When an update is ready, you'll see a notification to restart and apply it.

To check manually, open the **Kiro** menu and select **Check for Updates...** On Windows or Linux, open the Command Palette (`Ctrl + Shift + P`) and run `Kiro: Check for Updates`.

### Downgrade to a previous version

IDECLI

You can revert to an earlier version of Kiro IDE if an update introduces issues with your workflow.

1. Go to the [downloads page](https://kiro.dev/downloads/)

1. Scroll past the main download cards to the version list

1. Expand the version you want to install (for example, "IDE 0.12.x")

1. Download the installer for your platform

1. Uninstall your current version of Kiro:


    - **macOS:** drag Kiro from Applications to the Trash

    - **Windows:** uninstall from **Settings > Apps > Installed apps**

    - **Linux:** run `sudo apt remove kiro` or `sudo dnf remove kiro` depending on your package manager

1. Run the downloaded installer

Your settings, extensions, and sign-in state are preserved across reinstalls. When you're ready to move back to the latest version, download it from the [downloads page](https://kiro.dev/downloads/) or let the application update automatically.

### Uninstalling

IDECLI

Uninstall Kiro IDE using your operating system's standard application removal process (drag to Trash on macOS, Apps & Features on Windows, or your package manager on Linux).

### Proxy configuration

Kiro respects standard proxy environment variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`) on both the IDE and the CLI. Set these in your shell:

```bash
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
export NO_PROXY=localhost,127.0.0.1,.company.com
```

For proxies that require authentication:

```bash
export HTTPS_PROXY=http://username:password@proxy.company.com:8080
```

IDECLI

In addition to the environment variables, you can configure proxy settings in **Settings > Proxy** inside Kiro.

**Browser-based sign-in bypasses proxy settings**

When you sign in, Kiro opens your default browser. This browser traffic uses your operating system's network stack, not the IDE's proxy configuration.

For the full reference, including URLs to allowlist and data perimeter guidance, see [Firewalls, proxies, and data perimeters](https://kiro.dev/docs/privacy-and-security/firewalls/).

### Troubleshooting

IDECLI

For installation failures, network connectivity problems, sign-in errors, shell integration, and Windows-specific issues, see the [IDE troubleshooting guide](https://kiro.dev/docs/ide/troubleshooting/).

### Next steps

- [Authentication](https://kiro.dev/docs/getting-started/authentication/) — set up your sign-in method

- [Your first project](https://kiro.dev/docs/getting-started/first-project/) — guided walkthrough for new users

- [Language support](https://kiro.dev/docs/guides/languages-and-frameworks/typescript-javascript-guide/) — environment setup per language

Page updated:   September 2, 2026[Authentication](https://kiro.dev/docs/getting-started/authentication/)

---

# First Project

This guide walks you through Kiro's essential features by working with a real project. You'll learn how to set up steering files, build features with specs, automate workflows with hooks, and extend capabilities with MCP servers.

### Prerequisites

Before starting, ensure you have:

- [Installed Kiro](https://kiro.dev/docs/getting-started/installation/)

- [Signed in](https://kiro.dev/docs/getting-started/authentication/) with your Kiro account

- A project to work with (either an existing project or a new one)

- Basic familiarity with your project's structure and technology stack

### Open your project

IDECLIWebMobile

1. **Launch Kiro** and open your project:




    - Use `File > Open Folder` to select your project directory

    - Or drag and drop your project folder into Kiro

    - Or run `kiro .` from your project directory in the command line

1. **Access the Kiro Panel**:




    - Click the Kiro Ghost icon in the activity bar (left sidebar)

    - This panel provides access to all of Kiro's AI-powered features

1. **Start a Chat Session**:




    - The chat pane should be open by default

    - This opens Kiro's conversational interface where you interact with the AI

### Set up steering files

Steering files provide context about your project, helping Kiro understand your codebase, conventions, and requirements. They are stored in `.kiro/steering/` and shared across all Kiro surfaces.

IDECLIWebMobile

Choose **Generate Steering Docs** from the Kiro panel. Kiro analyzes your repository and generates steering documents that guide its behavior, including:

- Your product and its purpose

- Technical stack and frameworks

- Project structure and conventions

You can also create custom steering files by clicking the `+` button in the steering section to add coding standards, workflows, and team best practices.

[View transcript: Generating steering documents in Kiro](https://kiro.dev/transcripts/kiro-steering/)

Learn more about steering in the [Steering documentation](https://kiro.dev/docs/steering/).

### Build features with specs

Specs transform high-level feature ideas into detailed implementation plans through three phases:

1. **Requirements** - User stories with acceptance criteria

1. **Design** - Technical architecture and implementation approach

1. **Tasks** - Discrete, trackable implementation steps

IDECLIWebMobile

#### Create your first spec

1. **Start a new spec**:




    - Click the **Spec** button in your chat session

    - Or choose the `+` button in the Kiro panel's Specs section

1. **Enter a feature description**:




    - Describe your feature in natural language

    - Example: "Add a user authentication system with login, logout, and password reset functionality"

1. **Follow the guided workflow**:




    - **Requirements phase**: Kiro structures your requirements using EARS notation

    - **Design phase**: Technical architecture and component design are documented

    - **Implementation phase**: Discrete tasks are generated for execution

[View transcript: Creating a spec in Kiro](https://kiro.dev/transcripts/specs-start/)

#### Execute spec tasks

Once your spec is complete:

1. **Review generated tasks** in the `tasks.md` file

1. **Execute tasks** by clicking on individual task items

1. **Track progress** as tasks automatically update to "In Progress" and "Done"

Learn more about specs in the [Specs documentation](https://kiro.dev/docs/specs/).

### Automate workflows with hooks

Agent hooks eliminate manual work by automatically executing predefined actions when specific agent events occur, such as file changes, tool use, or task execution.

IDECLIWebMobile

1. **Access hook creation**:




    - Navigate to the **Agent Hooks** section in the Kiro panel

    - Click the `+` button to create a new hook

1. **Define hook behavior**:




    - Describe what you want automated in natural language

    - Example: "When the agent saves a React component file, automatically create or update its corresponding test file"

1. **Configure hook settings**:




    - **Event type**: Choose when the hook triggers - agent file events (created, saved, deleted), prompt and agent lifecycle events, or spec task events

    - **File pattern**: Specify which files should trigger the hook (e.g., `src/**/*.tsx`)

    - **Instructions**: Define the specific actions to perform

Learn more in the [Hooks documentation](https://kiro.dev/docs/hooks/).

### Extend capabilities with MCP

Model Context Protocol (MCP) allows Kiro to access specialized tools, APIs, knowledge bases, and external services.

IDECLIWebMobile

#### Set up MCP

1. Open the Kiro panel by clicking the Kiro Ghost icon in the activity bar. Enable MCPs, then click the edit button (pencil icon) next to MCP in the panel.

1. By default, Kiro ships with the [fetch MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch). Set `disabled` to `false` to connect to it.

1. Add any MCP server by editing the JSON file:

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

Once configured, reference MCP tools in several ways:

- **Direct questions**: Ask questions that leverage the server's capabilities

- **Explicit tool usage**: Reference specific tools with the `#MCP` context provider

- **Integration**: Combine MCP with hooks and specs for automated workflows

Learn more in the [MCP documentation](https://kiro.dev/docs/mcp/).

### Next steps

Now that you've experienced Kiro's core features:

- **Try the interactive tutorial**: Work through the [hands-on game development tutorial](https://kiro.dev/docs/guides/learn-by-playing/)

- **Explore specs in depth**: Check out the [Specs documentation](https://kiro.dev/docs/specs/) for the full workflow

- **Learn about steering**: Read the [Steering documentation](https://kiro.dev/docs/steering/) for advanced configuration

- **Join the community**: Connect with other Kiro users on [Discord](https://discord.gg/kirodotdev)

Page updated:   September 2, 2026[Authentication](https://kiro.dev/docs/getting-started/authentication/)[Models](https://kiro.dev/docs/models/)

---

# Steering & Guidance

### What is steering?

Steering gives Kiro persistent knowledge about your project through markdown files. Instead of explaining your conventions in every chat, steering files ensure Kiro consistently follows your established patterns, libraries, and standards.

| Capability | IDE | CLI | Web | Mobile |
| --- | --- | --- | --- | --- |
| Workspace steering (`.kiro/steering/`) | ✓ | ✓ | ✓ | ✓ |
| Global steering (`~/.kiro/steering/`) | ✓ | ✓ | — | — |
| Cloud steering managed in Web settings | — | — | ✓ | — |
| Generate foundation files via UI | ✓ | — | — | — |
| Inclusion modes (always, fileMatch, manual) | ✓ | ✓ | ✓ | ✓ |
| AGENTS.md support | ✓ | ✓ | ✓ | ✓ |

On Web, "Global steering" refers to your local `~/.kiro/steering/` directory, which the cloud sandbox cannot read. To reuse personal steering across cloud sessions, upload it through [Configuration Sync](https://kiro.dev/docs/web/cloud-configuration/); the cloud copy then applies to every cloud session.

### Key benefits

**Consistent Code Generation** - Every component, API endpoint, or test follows your team's established patterns and conventions.

**Reduced Repetition** - No need to explain project standards in each conversation. Kiro remembers your preferences.

**Team Alignment** - All developers work with the same standards, whether they're new to the project or seasoned contributors.

**Scalable Project Knowledge** - Documentation that grows with your codebase, capturing decisions and patterns as your project evolves.

### Steering file scope

Steering files can be created with a workspace scope or a global scope.

#### Workspace steering

Workspace steering files reside in your project root folder under `.kiro/steering/`, and apply only to that specific workspace. Workspace steering files can be used to inform Kiro of patterns, libraries, and standards that apply to an individual workspace.

#### Global steering

Global steering files reside in your home directory under `~/.kiro/steering/`, and apply to all workspaces. Global steering files can be used to inform Kiro of conventions that apply to *all* your workspaces.

In case of conflicting instructions between global and workspace steering, Kiro will prioritize the workspace steering instructions. This allows you to specify global directives that generally apply to all your workspaces, while preserving the ability to override those directives for specific workspaces.

#### Team steering

The global steering feature can be used to define centralized steering files that apply to entire teams. Team steering files can be pushed to user's PCs via MDM solutions or Group Policies, or downloaded by users to their PCs from a central repository, and placed into the `~/.kiro/steering` folder.

### Project steering files

Kiro provides project steering files to establish core project context:

**Product Overview** (`product.md`) - Defines your product's purpose, target users, key features, and business objectives. This helps Kiro understand the "why" behind technical decisions and suggest solutions aligned with your product goals.

**Technology Stack** (`tech.md`) - Documents your chosen frameworks, libraries, development tools, and technical constraints. When Kiro suggests implementations, it will prefer your established stack over alternatives.

**Project Structure** (`structure.md`) - Outlines file organization, naming conventions, import patterns, and architectural decisions. This helps generated code fit your existing codebase.

These foundation files are included in every interaction by default, forming the baseline of Kiro's project understanding.

IDECLIWeb

To generate project steering files in the IDE:

1. Navigate to the **Steering** section in the Kiro panel

1. Click the **Generate Steering Docs** button, or click the **+** button and select the **Foundation steering files** option

1. Kiro will create three project steering files in `.kiro/steering/`

### Creating custom steering files

Extend Kiro's understanding with specialized guidance tailored to your project's unique needs.

IDECLIWeb

1. Navigate to the **Steering** section in the Kiro panel

1. Click the **+** button

1. Select the scope of the steering file: workspace or global

1. Choose a descriptive filename (e.g., `api-standards.md`)

1. Write your guidance using standard markdown syntax

1. Use natural language to describe your requirements

1. Optionally, use the **Refine** button to have Kiro refine your requirements

Once created, steering files become immediately available across all Kiro interactions.

### Steering with custom agents

When using [custom agents](https://kiro.dev/docs/custom-agents/creating/), steering files are not automatically included. You must explicitly add them to the agent's `resources` configuration to load steering context.

To include all steering files in a custom agent, add the following to your agent configuration:

```json
{
  "resources": ["file://.kiro/steering/**/*.md"]
}
```

This glob pattern ensures all markdown files in your steering directory are loaded when using the agent. See the [custom agents documentation](https://kiro.dev/docs/custom-agents/creating/) for a complete configuration example.

### Agents.md

Kiro supports providing steering directives via the [AGENTS.md](https://agents.md/) standard. AGENTS.md files are in markdown format, similar to Kiro steering files; however, AGENTS.md files do not support [inclusion modes](#inclusion-modes) and are always included.

You can add AGENTS.md files to the global steering file location (`~/.kiro/steering/`), or to the root folder of your workspace, and they will get picked up by Kiro automatically.

AGENTS.md files are also discovered in subdirectories throughout your workspace. This lets you place an AGENTS.md next to the code it describes — for example, one in `services/api/` and another in `packages/ui/` — and each is loaded as steering context alongside your other steering files.

### Inclusion modes

Steering files can be configured to load at different times based on your needs. This flexibility helps optimize performance and ensures relevant context is available when needed.

Configure inclusion modes by adding front matter to the top of your steering files. The front matter uses YAML syntax and must be placed at the very beginning of the file, enclosed by triple dashes (`---`).

**Info**

The inclusion configuration must be the first content in the file - no blank lines or content before it.

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

**Usage**: Type `#troubleshooting-guide` or `#performance-optimization` in chat to include that steering file for the current conversation. Manual steering files also appear as slash commands - type `/` in chat to see and select them.

**Best for**: Specialized workflows, troubleshooting guides, migration procedures, or context-heavy documentation that's only needed occasionally.

#### Auto inclusion

```yaml
---
inclusion: auto
name: api-design
description: REST API design patterns and conventions. Use when creating or modifying API endpoints.
---
```

Files are automatically included when your request matches the description. This works similarly to [skills](https://kiro.dev/docs/skills/) - Kiro uses the description to decide when the steering file is relevant.

| Field | Required | Description |
| --- | --- | --- |
| `name` | Yes | Identifier for the steering file. Used for display and matching. |
| `description` | Yes | When to include this file. Kiro matches this against your requests. |

Auto-inclusion steering files also appear as slash commands in chat. Type `/` followed by the steering file name to explicitly include it, in addition to the automatic activation based on description matching.

**Best for**: Context-heavy guidance that should only load when relevant - like specialized domain knowledge, complex workflows, or detailed reference material that would overwhelm always-on steering.

**Info**

On Kiro CLI, inclusion modes are not currently supported. All steering files in the `.kiro/steering/` directory are loaded automatically.

### File references

Link to live workspace files to keep steering current:

```markdown
#[[file:<relative_file_name>]]
```

Examples:

- API specs: `#[[file:api/openapi.yaml]]`

- Component patterns: `#[[file:components/ui/button.tsx]]`

- Config templates: `#[[file:.env.example]]`

### Steering during a session

In addition to persistent steering files, you can steer Kiro in real time during any session by providing direction in the chat:

- "Use the repository's existing error handling pattern"

- "Follow the same approach as the UserService class"

- "Make sure to add integration tests, not just unit tests"

**Info**

On Kiro Web, the agent asks clarifying questions upfront in [autonomous mode](https://kiro.dev/docs/web/autonomous-mode/) - your answers act as steering for that task. In the default mode, you can steer continuously as you iterate together.

### Teaching through code reviews

On Kiro Web, you can steer the agent by leaving feedback on pull requests. When you comment on a PR with guidance like "always use our standard error handling" or "follow our naming conventions," the agent learns and applies those patterns to future work across all your repositories.

Only your feedback (the user who created the task) influences the agent's learnings. Other reviewers' comments don't affect what the agent learns.

### Best practices

**Keep Files Focused** - One domain per file - API design, testing, or deployment procedures.

**Use Clear Names**:

- `api-rest-conventions.md` - REST API standards

- `testing-unit-patterns.md` - Unit testing approaches

- `components-form-validation.md` - Form component standards

**Include Context** - Explain why decisions were made, not just what the standards are.

**Provide Examples** - Use code snippets and before/after comparisons to demonstrate standards.

**Security First** - Never include API keys, passwords, or sensitive data. Steering files are part of your codebase.

**Maintain Regularly**:

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

- [Skills](https://kiro.dev/docs/skills/) - On-demand modular instruction packages for specialized workflows

- [Hooks](https://kiro.dev/docs/hooks/) - Automate agent actions based on events

- [Custom Agents](https://kiro.dev/docs/custom-agents/) - Build specialized agents with tailored steering

Page updated:   September 2, 2026[Best practices](https://kiro.dev/docs/specs/best-practices/)[Hooks](https://kiro.dev/docs/hooks/)

---

# Spec-Driven Development

### What are specs?

Specs or specifications are structured artifacts that formalize the development process for features and bug fixes in your application. They provide a systematic approach to transform high-level ideas into detailed implementation plans with clear tracking and accountability.

| Capability | IDE | CLI | Web | Mobile |
| --- | --- | --- | --- | --- |
| Feature Specs | ✓ | ✓ | ✓ | — |
| Bugfix Specs | ✓ | ✓ | ✓ | — |
| Quick Spec | ✓ | ✓ | ✓ | — |
| Parallel task execution | ✓ | ✓ | ✓ | — |
| [Analyze Requirements](https://kiro.dev/docs/specs/analyze-requirements/) | ✓ | ✓ | — | — |
| [Correctness](https://kiro.dev/docs/specs/correctness/) (property-based testing) | ✓ | — | — | — |

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

IDECLIWeb

Kiro provides a task execution interface for `tasks.md` files that displays real-time status updates. Tasks are updated as in-progress or completed, allowing you to efficiently track implementation progress.

#### Running tasks in parallel

When you run all tasks on a spec, Kiro analyzes your task list, figures out which tasks depend on each other, and runs independent tasks concurrently. For most feature specs, this cuts execution time significantly without any setup.

Kiro builds a **dependency graph** of the tasks in your `tasks.md` and groups independent tasks into **waves**:

- **Wave 1** - all tasks with no dependencies. These run concurrently.

- **Wave 2** - all tasks whose dependencies were satisfied by Wave 1. These run concurrently.

- **Wave N** - continues until all tasks are complete.

Waves execute sequentially; tasks within a wave execute concurrently.



### Types of Specs

Kiro supports two types of specs to match your development needs:

#### Feature Specs

For building new features and capabilities in your application. Feature Specs guide you through requirements gathering, technical design, and implementation planning with two workflow variants: Requirements-First and Design-First. For well-understood features, you can also use [Quick Spec](https://kiro.dev/docs/specs/quick-spec/) to auto-generate all three artifacts without approval gates.

[Learn more about Feature Specs →](https://kiro.dev/docs/specs/feature-specs/)

#### Bugfix Specs

For systematically diagnosing and fixing bugs with surgical precision while preventing regressions. Bugfix Specs help you identify root causes, design fixes, and validate that nothing else breaks.

[Learn more about Bugfix Specs →](https://kiro.dev/docs/specs/bugfix-specs/)

### Getting Started

IDECLIWeb

1. From the Kiro pane, click the `+` button under **Specs**. Alternatively, choose **Spec** from the chat pane.

1. Kiro will ask if you are developing a Feature or fixing a Bug


    - If you choose Feature, describe your feature and choose your workflow: **Requirements-First** or **Design-First**

    - If you choose Bug, describe your bug

1. Follow the workflow through each phase to implementation

### Learn more

Go deeper into Kiro's Spec system with these guides:

[Feature SpecsBuild new features with structured workflows.](https://kiro.dev/docs/specs/feature-specs/)[Quick SpecGenerate requirements, design, and tasks in one pass without approval gates.](https://kiro.dev/docs/specs/quick-spec/)[Analyze RequirementsCatch inconsistencies, ambiguities, and gaps in your requirements before design.](https://kiro.dev/docs/specs/analyze-requirements/)[Bugfix SpecsFix bugs surgically while preventing regressions.](https://kiro.dev/docs/specs/bugfix-specs/)[Best PracticesFAQs on best practices when working with specs.](https://kiro.dev/docs/specs/best-practices/)Page updated:   August 27, 2026[How Kiro works](https://kiro.dev/docs/how-kiro-works/)[Feature Specs](https://kiro.dev/docs/specs/feature-specs/)

---

# Agent Hooks

Hooks run shell commands or agent prompts automatically when specific events happen in your session - the agent modifies a file, invokes a tool, or completes a task. You define the trigger and the action; Kiro handles the execution.

| Capability | IDE | CLI | Web | Mobile |
| --- | --- | --- | --- | --- |
| Event-driven hooks | ✓ | ✓ | ✓ | — |
| Shell command actions | ✓ | ✓ | ✓ | — |
| Agent prompt actions | ✓ | ✓ | ✓ | — |
| Create Hooks by asking the agent in chat | ✓ | ✓ | ✓ | — |

### What you can do with hooks

- **Enforce standards** - run linters, formatters, or type checks automatically after agent file changes

- **Gate dangerous operations** - block tool execution unless preconditions are met (PreToolUse)

- **Generate companion files** - auto-create tests, docs, or translations when new source files appear

- **Validate before commit** - check code quality before the agent finalizes changes

- **Inject context** - feed the agent additional instructions based on what it's doing

### Quick example

A `PostFileSave` hook that runs ESLint whenever the agent saves or edits a TypeScript file:

```json
{
  "version": "v1",
  "hooks": [{
    "name": "Lint on save",
    "trigger": "PostFileSave",
    "matcher": "\\.(ts|tsx)$",
    "action": { "type": "command", "command": "npx eslint --fix" }
  }]
}
```

This file lives at `.kiro/hooks/lint-on-save.json` and activates automatically - no manual prompting needed. The hook receives the saved file path and session context via STDIN. See [Hook Actions](https://kiro.dev/docs/hooks/actions/) for details on how commands receive event data.

### How hooks work

Hook configurations are JSON files stored in `.kiro/hooks/`. Each file defines one or more hooks with a trigger event, an optional matcher pattern, and an action.

When the trigger event fires, Kiro checks the matcher. If it matches (or no matcher is specified), the action executes:

- **Command actions** run a shell command in your project root. The command receives session context as JSON on STDIN.

- **Agent actions** inject a prompt into the current conversation, steering the agent's behavior.

#### Available triggers

| Trigger | When it fires | IDE | CLI | Web | Can block? |
| --- | --- | --- | --- | --- | --- |
| [Prompt Submit](https://kiro.dev/docs/hooks/types/#prompt-submit) | When a message is sent to the agent | ✓ | ✓ | — | Yes |
| [Agent Stop](https://kiro.dev/docs/hooks/types/#agent-stop) | When the agent finishes responding | ✓ | ✓ | — | No |
| [Session Start](https://kiro.dev/docs/hooks/types/#session-start-ide-only) | When a new session begins (IDE) | ✓ | — | — | No |
| [Agent Spawn](https://kiro.dev/docs/hooks/types/#agent-spawn-cli-only) | When the agent is activated (CLI) | — | ✓ | — | No |
| [Pre Tool Use](https://kiro.dev/docs/hooks/types/#pre-tool-use) | Before a tool is about to execute | ✓ | ✓ | — | Yes |
| [Post Tool Use](https://kiro.dev/docs/hooks/types/#post-tool-use) | After a tool has executed | ✓ | ✓ | — | No |
| [File Create](https://kiro.dev/docs/hooks/types/#file-create) | After the agent creates a new file | ✓ | — | — | No |
| [File Save](https://kiro.dev/docs/hooks/types/#file-save) | After the agent saves or edits a file | ✓ | — | — | No |
| [File Delete](https://kiro.dev/docs/hooks/types/#file-delete) | After the agent deletes a file | ✓ | — | — | No |
| [Pre Task Execution](https://kiro.dev/docs/hooks/types/#pre-task-execution-ide-only) | Before a spec task starts | ✓ | — | — | Yes |
| [Post Task Execution](https://kiro.dev/docs/hooks/types/#post-task-execution-ide-only) | After a spec task completes | ✓ | — | — | No |
| [Legacy Manual Hook](https://kiro.dev/docs/hooks/types/#legacy-manual-hooks-ide-only) | Legacy IDE 0.x hooks, run manually | Legacy only | — | — | No |

**Info**

File triggers respond only to changes made by the agent. Saving, creating, or deleting a file manually in the editor does not trigger `PostFileSave`, `PostFileCreate`, or `PostFileDelete`.

**Info**

Existing manual Hooks from IDE 0.x continue to appear as legacy Hooks and can still be run from the Agent Hooks panel. To create a new on-demand workflow, create a [manually included Steering file](https://kiro.dev/docs/steering/#manual-inclusion) instead.

See [Hook Triggers](https://kiro.dev/docs/hooks/types/) for detailed descriptions, matcher patterns, and use cases for each trigger type.

### Hook file schema

Each hook file is a standalone JSON file at `.kiro/hooks/<id>.json`. The full schema:

```json
{
  "version": "v1",
  "hooks": [
    {
      "name": "example-hook",
      "trigger": "PostFileSave",
      "matcher": "\\.(ts|tsx)$",
      "action": { "type": "command", "command": "npx eslint --fix" }
    }
  ]
}
```

#### Field reference

| Field | Required | Description |
| --- | --- | --- |
| `version` | Yes | Schema version - currently `"v1"` |
| `hooks` | Yes | Array of hook definitions |
| `hooks[].name` | Yes | Human-readable identifier for the hook |
| `hooks[].description` | No | Documentation only |
| `hooks[].trigger` | Yes | Event that fires the hook (PascalCase - see [triggers table](#available-triggers)) |
| `hooks[].matcher` | No | Regex pattern to filter which events fire this hook. For `PreToolUse`/`PostToolUse`, matches tool name. For file events, matches file path. Defaults to always-match. |
| `hooks[].action.type` | Yes | `"command"` (shell command) or `"agent"` (inject prompt) |
| `hooks[].action.command` | Cond. | Shell command to run (required when `type` is `"command"`) |
| `hooks[].action.prompt` | Cond. | Prompt text to inject (required when `type` is `"agent"`) |
| `hooks[].timeout` | No | Timeout in seconds for command actions (default: 60). `0` disables the timeout. Ignored for agent actions. |
| `hooks[].enabled` | No | Set `false` to skip the hook without deleting it (default: `true`) |
| `hooks[].confirm` | No | Ask for confirmation before a `Stop` command hook runs. See [Confirmation prompts](#confirmation-prompts). |

#### Confirmation prompts

A command hook on the `Stop` trigger can ask before it runs. Add a `confirm` block with the question to ask and the options to present:

```json
{
  "version": "v1",
  "hooks": [
    {
      "name": "Submit session results",
      "trigger": "Stop",
      "action": { "type": "command", "command": "./submit.sh" },
      "confirm": {
        "question": "Submit this session's results?",
        "options": [
          { "id": "submit", "label": "Yes, submit", "run": true },
          { "id": "dismiss", "label": "Not this time", "run": false }
        ]
      }
    }
  ]
}
```

Each option has an `id`, a `label` shown on the button, and a `run` flag that controls whether the hook's command executes when that option is chosen.

##### Dynamic confirm options with `confirmCommand`

To decide at run time whether and what to ask, add an optional `confirmCommand` to the `confirm` block. The command runs before the prompt appears, and its stdout controls the prompt as JSON:

- `{ "skip": true }` suppresses the prompt and skips the hook for this turn

- `{ "question": "...", "options": [...] }` replaces the static question and options

```json
{
  "confirm": {
    "question": "Submit this session's results?",
    "confirmCommand": "./confirm-options.sh",
    "options": [
      { "id": "submit", "label": "Yes, submit", "run": true },
      { "id": "dismiss", "label": "Not this time", "run": false }
    ]
  }
}
```

If `confirmCommand` exits non-zero, times out, or prints invalid JSON, the static `question` and `options` are used as a fallback. This makes it useful for prompts that should only appear under certain conditions - for example, a "don't ask again this session" option that writes a marker file and returns `{ "skip": true }` on later turns.

#### File naming and location

- **Location**: `.kiro/hooks/` in your project root

- **Naming**: Any `.json` filename works - use descriptive kebab-case names (e.g., `lint-on-save.json`, `guard-writes.json`)

- **Multiple hooks per file**: A single file can define multiple hooks in the `hooks` array

- **Activation**: Hooks activate automatically when a session starts - no manual registration needed

### Setting up hooks

IDECLIWeb

Click the **+** button in the Agent Hooks section of the Kiro panel and select **Ask Kiro to create a hook**. Describe what you want in natural language - for example, "run tests after every file save" - and Kiro generates the hook configuration through conversation.

The resulting hook is saved as a JSON file in `.kiro/hooks/`.

### Previous versions

The `.kiro/hooks/*.json` format was introduced in **IDE 1.0** and **CLI 3.0**. If you're upgrading from an earlier version:

- **From IDE 0.x** - Hooks moved from the previous format to standalone JSON files with PascalCase trigger names. See [What's new in IDE 1.0: Hooks](https://kiro.dev/docs/ide/whats-new-v1/hooks/) for the trigger mapping.

- **From CLI 2.x** - Hooks moved from embedded fields in agent config to standalone files. Run `kiro-cli agent migrate` to auto-convert, or see [CLI 3.0 Hooks migration](https://kiro.dev/docs/cli/v3/hooks-migration/) for the manual mapping.

### Next steps

- **[Hook Triggers](https://kiro.dev/docs/hooks/types/)** - Trigger types and their use cases

- **[Hook Actions](https://kiro.dev/docs/hooks/actions/)** - Command and agent action details

- **[Management](https://kiro.dev/docs/hooks/management/)** - Organize, edit, and maintain hooks

- **[Best Practices](https://kiro.dev/docs/hooks/best-practices/)** - Patterns for effective hook design

- **[Examples](https://kiro.dev/docs/hooks/examples/)** - Templates you can use

- **[Troubleshooting](https://kiro.dev/docs/hooks/troubleshooting/)** - Common issues and solutions

Page updated:   September 2, 2026[Steering](https://kiro.dev/docs/steering/)[Hook triggers](https://kiro.dev/docs/hooks/types/)

---

# Model Context Protocol (MCP)

Model Context Protocol (MCP) extends Kiro's capabilities by connecting to specialized servers that provide additional tools and context. This guide helps you set up, configure, and use MCP servers with Kiro across all surfaces.

| Capability | IDE | CLI | Web | Mobile |
| --- | --- | --- | --- | --- |
| Local (stdio) MCP servers | ✓ | ✓ | ✓ | — |
| Remote (HTTP/SSE) MCP servers | ✓ | ✓ | ✓ | — |
| MCP config file (JSON) | ✓ | ✓ | ✓ | — |
| Server-provided prompts and resources | ✓ | ✓ | ✓ | — |

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

#### Adding an MCP server

IDECLIWeb1

##### Open the MCP configuration

Open the command palette (`Cmd + Shift + P` on Mac, `Ctrl + Shift + P` on Windows/Linux) and search for **Kiro: Open workspace MCP config (JSON)** or **Kiro: Open user MCP config (JSON)**.

Alternatively, open the Kiro panel and select the **Open MCP Config** icon.

2

##### Add your server configuration

```json
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"],
      "disabled": false
    }
  }
}
```

3

##### Save and verify

Save the config file (`Cmd+S`). Servers reconnect automatically. Check the MCP servers tab in the Kiro panel to confirm the server is connected.

#### Installing from an install link

Some server directories and websites offer one-click install links that use the `kiro://` URL scheme. Opening one of these links doesn't change your setup immediately: Kiro shows a confirmation dialog before anything is written to your configuration. The dialog lists the command that will run and its arguments, along with the names of any environment variables or headers - their values stay hidden. Review the details and confirm to add the server, or cancel to leave your configuration unchanged.

**Warning**

Only install MCP servers from sources you trust. See [Security best practices](https://kiro.dev/docs/mcp/security/) for guidance on evaluating servers before installing them.

#### Agent configuration

You can also define MCP servers directly in an agent's configuration file. The `mcpServers` field specifies which MCP servers the agent has access to:

```json
{
  "name": "myagent",
  "description": "My special agent",
  "mcpServers": {
    "fetch": {
      "command": "fetch3.1",
      "args": []
    }
  },
  "includeMcpJson": false
}
```

The `includeMcpJson` field determines whether to include MCP servers defined in workspace and user-level configuration files. When set to `true`, the agent has access to all MCP servers defined in user and workspace-level configurations in addition to those defined in the agent's `mcpServers` field.

### Troubleshooting

#### Checking MCP logs

IDECLI

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

#### Tool validation errors

If you see "The following tools have been excluded due to validation errors", the tool fails one of these requirements:

- Tool name exceeds 64 characters (including server prefix)

- Tool name contains invalid characters (must match `^[a-zA-Z][a-zA-Z0-9_]*$`)

- Tool description is empty

Contact the MCP server maintainer to fix the tool specification.

#### Large description warnings

If you see "The following tools have large descriptions which may impact agent performance", a tool description exceeds 10,000 characters. The tool still works but may slow down responses. Consider asking the server maintainer to shorten the description.

### Additional resources

- [Official MCP Documentation](https://modelcontextprotocol.io/introduction)

### Next steps

- **[Configuration](https://kiro.dev/docs/mcp/configuration/)** - Detailed configuration options and file structure

- **[Server directory](https://kiro.dev/docs/mcp/servers/)** - Browse available MCP servers

- **[Tools](https://kiro.dev/docs/mcp/usage/)** - Learn how to use MCP tools effectively

- **[Best practices](https://kiro.dev/docs/mcp/security/)** - Security best practices for MCP usage

Page updated:   September 2, 2026[Troubleshooting](https://kiro.dev/docs/hooks/troubleshooting/)[Configuration](https://kiro.dev/docs/mcp/configuration/)

---

# Command Line Interface (CLI)

The Kiro CLI brings the power of AI-assisted development to your terminal. Build, test, and deploy applications using natural language commands and automated workflows.

Get started with the Kiro CLI in minutes.

Install on  macOS ,  Linux , or Windows`curl -fsSL https://cli.kiro.dev/install | bash`

Start using Kiro CLI:

```bash
cd my-project
kiro-cli
```

### CLI-unique features

[Interactive ChatEngage with Kiro through natural conversation in your terminal.](https://kiro.dev/docs/cli/chat/)[Terminal UIRich terminal experience with syntax highlighting, panels, and themes.](https://kiro.dev/docs/cli/terminal-ui/)[Headless ModeRun prompts non-interactively in CI/CD pipelines with API keys.](https://kiro.dev/docs/cli/headless/)[Voice ModeDictate prompts hands-free with local Whisper speech-to-text.](https://kiro.dev/docs/cli/voice/)[ACPAgent Communication Protocol for programmatic agent interactions.](https://kiro.dev/docs/cli/acp/)[Auto CompleteIntelligent command completion with context awareness.](https://kiro.dev/docs/cli/autocomplete/)[Code IntelligenceLanguage-aware code understanding and navigation.](https://kiro.dev/docs/tools/code-intelligence/)

### Shared capabilities

The Kiro CLI uses the same core capabilities as every other Kiro surface. See the Features section for full documentation:

- [Steering](https://kiro.dev/docs/steering/) — Guide Kiro with project-specific context and conventions

- [Hooks](https://kiro.dev/docs/hooks/) — Automate actions before and after commands

- [MCP](https://kiro.dev/docs/mcp/) — Connect external tools and data sources

- [Custom agents](https://kiro.dev/docs/custom-agents/) — Build specialized agents for your workflows

- [Skills](https://kiro.dev/docs/skills/) — Extend Kiro with reusable skill packages

- [Sub-agents](https://kiro.dev/docs/custom-agents/subagents/) — Delegate focused work to agents that run in parallel

- [Models](https://kiro.dev/docs/models/) — Configure which AI models to use

- [Permissions](https://kiro.dev/docs/permissions/) — Manage capability-based access controls

### Use cases

The Kiro CLI is ideal for:

- **Interactive Development**: Chat with Kiro directly in your terminal for instant help

- **Headless Automation**: Run prompts non-interactively in CI/CD pipelines using [API key authentication](https://kiro.dev/docs/cli/headless/)

- **Custom Automation**: Create specialized agents for your specific workflows

- **Team Standardization**: Use team-level best practices and preferences

- **External Integrations**: Connect tools and services through MCP servers

- **Intelligent Assistance**: Get context-aware suggestions and auto-completion

- **Workflow Optimization**: Automate repetitive tasks with smart hooks

Page updated:   August 4, 2026[0.x reference](https://kiro.dev/docs/ide/0x-reference/)[What's new in 3.0](https://kiro.dev/docs/cli/v3/)

---

# Web Interface

Kiro Web is a browser-based development agent that helps you build software through conversation. Chat with the agent to discuss approaches, write code, and open pull requests or merge requests from [app.kiro.dev](https://app.kiro.dev).

Kiro Web is available on Pro, Pro+, Pro Max, and Power plans.

Kiro Web gives you three ways to work:

- Use the default mode to collaborate with the agent interactively and iterate on a problem together.

- Use [Spec mode](https://kiro.dev/docs/specs/) to shape requirements, a technical design, and an implementation plan before execution starts.

- Use [autonomous mode](https://kiro.dev/docs/web/autonomous-mode/) to delegate an outcome from planning through implementation and a pull request or merge request.

In every workflow, you review the result before it reaches your repository's default branch. Kiro never merges changes automatically.

### Prerequisites

- A Pro, Pro+, Pro Max, or Power subscription

- A [GitHub or GitLab repository provider connected](https://kiro.dev/docs/web/setup/) to Kiro

### AWS Identity Center

If your organization uses AWS Identity Center, your administrator must first enable Cloud Sessions by toggling on **Cloud Sessions** in **Settings > Kiro Settings**, in the AWS account where Kiro is configured. See [AWS Identity Center](https://kiro.dev/docs/web/identity-center/) for the full steps. Kiro Web is available in **US East (N. Virginia) `us-east-1`** only.

### Get started

[Repository setupConnect GitHub or GitLab and configure access](https://kiro.dev/docs/web/setup/)[Working with the agentChat, iterate, and open pull requests](https://kiro.dev/docs/web/using-the-agent/)

### Features

[Autonomous modeLet the agent own the outcome — it plans, codes, and opens PRs](https://kiro.dev/docs/web/autonomous-mode/)[SpecsShape requirements, a technical design, and an implementation plan, then have the agent implement and open a PR](https://kiro.dev/docs/specs/)[AutomationsSchedule recurring tasks on a cron — Kiro runs and opens PRs automatically](https://kiro.dev/docs/web/automations/)[MemorySee what the agent learns from your work over time](https://kiro.dev/docs/web/memory/)[SandboxIsolated execution environment with configurable access controls](https://kiro.dev/docs/web/sandbox/)[GitHub integrationRepositories, branches, pull requests, and issue-based tasks](https://kiro.dev/docs/web/github/)[GitLab integrationAdd a GitLab project, work on it, and open a merge request](https://kiro.dev/docs/web/gitlab/)

### Shared capabilities

Kiro Web uses the same core capabilities as the IDE and CLI. See the Features section for full documentation:

- [Cloud sessions](https://kiro.dev/docs/cloud-sessions/) — how the sandbox-backed sessions behind Kiro Web work, and how the IDE and CLI attach to them

- [Steering](https://kiro.dev/docs/steering/) — guide the agent with your team's standards and conventions

- [MCP](https://kiro.dev/docs/mcp/) — extend the agent with custom tool integrations

- [Powers](https://kiro.dev/docs/powers/) — install ready-made tool packs

- [Models](https://kiro.dev/docs/models/) — available AI models

Page updated:   September 2, 2026[Troubleshooting](https://kiro.dev/docs/crew/troubleshooting/)[Setup & First Run](https://kiro.dev/docs/web/setup/)

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

Page updated:   August 4, 2026[Java](https://kiro.dev/docs/guides/languages-and-frameworks/java-guide/)[Setup dev environment and launch the game](https://kiro.dev/docs/guides/learn-by-playing/00-setup/)

---

# Privacy & Security

Kiro is an AWS application that works as a standalone agentic IDE. Kiro's security framework is built around AWS's security infrastructure and follows practices to protect your development environment and data. Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud:

- Security of the cloud – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Kiro, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).

- Security in the cloud – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company's requirements, and applicable laws and regulations

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

- You can interrupt at any time and revert changes via **Revert all changes** or [checkpoints](https://kiro.dev/docs/checkpoints/).

#### Supervised mode

In Supervised mode, Kiro works interactively, pausing for your review after each turn:

- After the agent modifies files, it pauses and presents a diff for your review.

- You can accept individual changes (hunk-level granularity) or reject them to revert.

- The agent asks clarifying questions when needed.

- To reduce interruptions, consecutive edits to the same file may be batched.

Supervised mode is best suited for situations where you want to closely review agent output. For example, when working in an unfamiliar codebase, making changes to critical paths, or onboarding a new team member to agent-assisted workflows.

#### Choosing the right mode

Use **Autopilot** when you trust the task scope and want the agent to work efficiently without interruption. Use **Supervised** when you want to review each set of changes before they persist. In both cases, apply the security controls described in [best practices](#best-practices) to protect sensitive files, credentials, and infrastructure.

When operating in either mode, you can view individual or all file changes made by the agent by selecting **View all changes** in the **Chat** module. You can also select **Revert all changes** or revert to a [checkpoint](https://kiro.dev/docs/checkpoints/) to restore your files to their previous state.

### Trusted commands

By default, Kiro requires approval before running any command. You can create your own trusted commands list by searching for **Kiro Agent: Trusted Commands** in your settings.

Kiro uses simple string prefix matching to determine if a command should be automatically trusted:

- **Exact matching**: Commands must match exactly (e.g., `npm install`)

- **Wildcard matching**: Use `*` to trust command variations (e.g., `npm *` trusts all npm commands)

- **Universal trust**: Use `*` alone to trust all commands (use with extreme caution)

The system treats entire commands as single strings and only checks if they start with trusted patterns. It does not analyze command structure, chains, or special characters, putting full responsibility on you to carefully configure trusted patterns.

### Protected paths

Kiro requires explicit approval before writing to certain protected paths, preventing unintended modifications to sensitive workspace configuration files. This applies in both Autopilot and Supervised mode — when the agent attempts to create or modify a file matching a protected pattern, you see a confirmation prompt and the change is not applied until you approve it. If you decline, the agent skips the write and continues with the rest of the task.

**Info**

Protected paths are enforced in the Kiro IDE. In the CLI, trusted commands and workspace isolation serve as the primary access controls.

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

Kiro provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don't represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.

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

Kiro supports Open VSX extensions, including remote SSH extensions (the community-maintained [Open Remote - SSH](https://open-vsx.org/extension/jeanp413/open-remote-ssh) extension on Open VSX is a popular choice), to provide a familiar development experience. For comprehensive information about extension compatibility and support in Kiro, see our [extension compatibility guide](https://kiro.dev/docs/upgrade-guides/migrating-from-vscode/#extension-compatibility).

By following these practices, you can enjoy Kiro's capabilities while maintaining appropriate security boundaries for your development environment.

Page updated:   August 4, 2026[Supported regions](https://kiro.dev/docs/enterprise/supported-regions/)[Data protection](https://kiro.dev/docs/privacy-and-security/data-protection/)
