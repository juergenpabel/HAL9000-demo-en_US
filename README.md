# HAL9000-kalliope_demo-en_US
In this respository all configuration (and data) files are with english language resources, its primary purpose is to
serve as a demo configuration for my [HAL9000 digital-voice-assistant](https://github.com/juergenpabel/HAL9000).

Because multiple components of my project require language-specific configurations (primarily 'kalliope' and 'brain') and
these configurations are pulled into that project as git submodules in their respective locations within the repository, 
the actual configurations in this repository are stored (only) inside branches with corresponding names. With this 
setup, I can maintain all (demo-)configurations for my project in a single repository (this one) and add git submodule 
references to a correspponding branch in this repository (for english, I will create a similar demo-configuration 
repository for at least the german language later on).
