<!-- Start -->
<a id="readme-top"></a>



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="[https://github.com/othneildrew/Best-README-Template](https://github.com/levi549/Rebecca/tree/main)">
    <img src="images/robo.png" alt="Logo" width="110" height="110">
  </a>

  <h3 align="center">Rebecca - AI Agent for fairs and events!</h3>

  <p align="center">
    Explore Rebecca's documentation:
    <br />
    <a href="https://docs.google.com/document/d/1gp94SfoiHp7q1uv4GKJa6vzyX8j3ONkQ-zVp_nWaJd4/edit?usp=drivesdk"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="">View Demo</a>
    &middot;
    <a href="https://wa.me/5519992236931?text=Hi!%20I'd%20like%20to%20report%20a%20bug%20or%20share%20a%20suggestion%20to%20improve%20the%20project.">Report Bug</a>
    &middot;
  </p>
</div>






<!-- ABOUT THE PROJECT -->
## About The Project


Rebecca is an AI agent designed to interact, assist, and promote content at tech fairs and events. Powered by an advanced learning model, she assimilates and stores comprehensive information about the event and its hosting institutions, allowing her to answer visitor questions accurately and naturally.

Beyond just a conversational assistant, Rebecca is an active promoter. By moving autonomously throughout the venue, she acts as a dynamic advertising platform, broadcasting announcements through speech and displaying promotional content directly on her physical structure.





<br>

### Built With

Essential technologies and hardware components that bring Rebecca to life:

* [![Python][Python-shield]][Python-url]
* [![JSON][JSON-shield]][JSON-url]
* [![Raspberry Pi][Raspberry-shield]][Raspberry-url]
* [![Docker][Docker-shield]][Docker-url]
* [![Google Cloud][GCP-shield]][GCP-url]





## Getting Started

Follow these instructions to get a local copy of Rebecca up and running on your PC for development and testing.

### Prerequisites

To run Rebecca locally, you will need Python installed on your machine. We also use `uv` for lightning-fast package management.

* **Python**
  Download and install Python from the official website: [python.org/downloads](https://www.python.org/downloads/)
  > **⚠️ IMPORTANT FOR WINDOWS USERS:** During the installation, make sure to check the box **"Add Python to PATH"** at the bottom of the installer window. This is required so you can use the `pip` command directly in your terminal.

* **uv (Package Manager)**
  Once Python is installed and added to your PATH, install `uv` by running the following command in your terminal:
  
  **Windows (CMD/PowerShell):**
  ```cmd
  pip install uv
<br>

### Installation

Follow these steps to get your local environment set up:

1. **Clone the repo or download the ZIP**
   You can either download the repository as a ZIP file and extract it, or clone it using Git:
   
   ```CMD
   
   git clone [https://github.com/levi549/Rebecca.git](https://github.com/levi549/Rebecca.git)
<br>

2. **Navigate to the project directory**
   Open your terminal (CMD or PowerShell) and go to the folder where you extracted or cloned the project:
   
   ```CMD
   cd /Directory_Path
    ```
   <br>
   
 3. **Running the Project**
    To start the application, run the following command in your terminal:

    ```CMD
     uv run RebeccaMain/RebeccaMain.py
    ```

<br>
<!-- USAGE EXAMPLES -->

## ⚙️ Configuration & Usage

To use this project, you will need a **Gemini API Key**. Follow the steps below to get yours and configure the application:

1. Go to [Google AI Studio](https://aistudio.google.com/app/api-keys).
2. Sign in with your Google account.
3. Click on the **"Create API key"** button.
4. Copy the generated token.
5. Open the `RebeccaMain/Apikey.py` file in your code editor.
6. Replace `Your_ApiKey` with the API key you just copied.

> **⚠️ Security Warning:** Never commit your API key directly to GitHub! Make sure that `RebeccaMain/Apikey.py` is added to your `.gitignore` file before pushing any changes.


<br>
<!-- CONTRIBUTING -->

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:
<a href="https://github.com/levi549/Rebecca/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=levi549/Rebecca" />
</a>



<!-- LICENSE -->


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



<!-- CONTACT -->
## Contact

Rebecca Suporte - Rebecca@etec.gov.br

Project Link: [https://github.com/levi549/Rebecca]((https://github.com/levi549/Rebecca))



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

We would like to express our deepest gratitude to the people and teams who made this project possible:

* **[Professor Rafael Cruz](https://www.linkedin.com/in/rafael-cruz-73917212)** * **[Professor Tiago Jesus](https://www.linkedin.com/in/tiagojsouza)** * **Centro Paula Souza (CPS) Robotics Team** ```

---





[contributors-shield]: https://img.shields.io/github/contributors/levi549/Rebecca.svg?style=for-the-badge
[contributors-url]: https://github.com/levi549/Rebecca/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/levi549/Rebecca.svg?style=for-the-badge
[forks-url]: https://github.com/levi549/Rebecca/forks

[stars-shield]: https://img.shields.io/github/stars/levi549/Rebecca.svg?style=for-the-badge
[stars-url]: https://github.com/levi549/Rebecca/stargazers

[issues-shield]: https://img.shields.io/github/issues/levi549/Rebecca.svg?style=for-the-badge
[issues-url]: https://github.com/levi549/Rebecca/issues

[license-shield]: https://img.shields.io/github/license/levi549/Rebecca.svg?style=for-the-badge
[license-url]: https://github.com/levi549/Rebecca/blob/main/LICENSE
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white

[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[JSON-shield]: https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white
[JSON-url]: https://www.json.org/
[Raspberry-shield]: https://img.shields.io/badge/Raspberry%20Pi-C51A4A?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white
[Raspberry-url]: https://www.raspberrypi.org/
[Docker-shield]: https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[GCP-shield]: https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google%20cloud&logoColor=white
[GCP-url]: https://cloud.google.com/
