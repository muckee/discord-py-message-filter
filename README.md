<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/muckee/discord-py-message-filter">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Discord Python Message Filter</h3>

  <p align="center">
    A discord bot which filters messages for specified keywords or regular expressions.
    <br />
    <a href="https://github.com/muckee/discord-py-message-filter"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/muckee/discord-py-message-filter">View Demo</a>
    ·
    <a href="https://github.com/muckee/discord-py-message-filter/issues">Report Bug</a>
    ·
    <a href="https://github.com/muckee/discord-py-message-filter/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This library was written to act as a simple boilerplate for developing a message filter for Discord. Messages are compared against the strings in `expressions.json` and are deleted where there are matches.

Each string can be formatted as either plain-text, or as a regular expression - the value of the 'type' property of each expression must equal 'string' or 'regex', respectively, as can be seen in the example.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![wheel][wheel]][wheel-url]
* [![python-dotenv][python-dotenv]][python-dotenv-url]
* [![discord-py-interactions][discord-py-interactions]][discord-py-interactions-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The following instructions will explain how to download, install and run the application locally. Instructions for deploying this application in a production environment are beyond the scope of this application.

### Prerequisites

It is necessary to install the following software in order for the application to run properly.

* python
  ```sh
  apt install python3 pip
  ```
* dependencies
  ```sh
  pip install python-dotenv discord-py-interactions
  ```

Create an application with a bot from within the Discord Developer Portal.

The only privileged intent required is the 'Message Content Intent'.

The only permissions required when inviting the bot to a server are the 'manage messages' and 'read messages/view channels' permissions.

### Installation

1. Clone the repo
  ```sh
  git clone https://github.com/muckee/discord-py-message-filter.git
  ```
2. Update environment variables
  ```sh
  cd discord-py-message-filter
  cp .env.sample .env
  vi .env
  ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can start the bot by running `python3 main.py` from inside the project's root directory.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->

See the [open issues](https://github.com/muckee/discord-py-message-filter/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the EPL-2.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Muckee - [@muckee_eth](https://twitter.com/muckee_eth) - muckee@clonesoftheapocalypse.com.com

Project Link: [https://github.com/muckee/discord-py-message-filter](https://github.com/muckee/discord-py-message-filter)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Donations

If this library has helped you to make a bag, please consider making a donation to one of the following addresses:

- ***Solana:*** 7tKA18pUNF3hHBTMWd1BFfj1iVcggKbcB1TxxJnrhiKW
- ***Monero:*** 857PeoGenpWLGDQNPGYHohRa6EmxocCYWDyDnQvNChbtXBhZQgrr3BW6Vjvpy4EiZrBMqgfdH2bCcRzxKu6yy54TMXRTMQ3
- ***Ravencoin:*** RGN5nDGsU51EriSYA4RAddregrS2LzB5FJ
- ***Bitcoin:*** bc1qkajr4e9lqq9elk6pdafk7x3x8kk9zqlndrxuh8
- ***Stellar:*** GD6KWYMF6T3ZQ7DFC4AEKSMAEZL7FCSDFPTN6VKHBVM4YYOGXF4VM2XY
- ***Near:*** 349d3b53b98040c6ecafa3759beb9f39a025d32bb4db51baab7652af6a0d67bb
- ***ETH/BNB/MATIC:*** 0xE078B9524549585d6eF21542a7927751b2a85E89


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/muckee/discord-py-message-filter.svg?style=for-the-badge
[contributors-url]: https://github.com/muckee/discord-py-message-filter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/muckee/discord-py-message-filter.svg?style=for-the-badge
[forks-url]: https://github.com/muckee/discord-py-message-filter/network/members
[stars-shield]: https://img.shields.io/github/stars/muckee/discord-py-message-filter.svg?style=for-the-badge
[stars-url]: https://github.com/muckee/discord-py-message-filter/stargazers
[issues-shield]: https://img.shields.io/github/issues/muckee/discord-py-message-filter.svg?style=for-the-badge
[issues-url]: https://github.com/muckee/discord-py-message-filter/issues
[license-shield]: https://img.shields.io/github/license/muckee/discord-py-message-filter.svg?style=for-the-badge
[license-url]: https://github.com/muckee/discord-py-message-filter/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/github/pipenv/locked/python-version/muckee/discord-py-message-filter
[Python-url]: https://www.python.org/
[wheel]: https://img.shields.io/github/pipenv/locked/dependency-version/muckee/discord-py-message-filter/wheel
[wheel-url]: https://pythonwheels.com/
[python-dotenv]: https://img.shields.io/github/pipenv/locked/dependency-version/muckee/discord-py-message-filter/python-dotenv
[python-dotenv-url]: https://pypi.org/project/python-dotenv/
[discord-py-interactions]: https://img.shields.io/github/pipenv/locked/dependency-version/muckee/discord-py-message-filter/discord-py-interactions
[discord-py-interactions-url]: https://pypi.org/project/discord-py-interactions/
