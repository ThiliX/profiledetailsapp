# Profile Details Mobile App (React Native)

A mobile profile application built with React Native and Expo, reproducing the profile details UI specification from `sample.png`.

## Preview & Features

- **App Bar**: Dark header with "My Profile" title.
- **Profile Avatar**: Circular user avatar with verified badge.
- **User Details**:
  - **Name**: Diluka
  - **Email**: diluka.w@nsbm.ac.lk (with mail icon)
  - **Points**: Dynamic points counter (with star icon)
- **Floating Action Button (FAB)**: Interactive button in the bottom right corner that increments points on press.
- **Cross-Platform**: Supports iOS, Android, and Web.

## Tech Stack

- **Framework**: React Native with Expo SDK 57
- **Icons**: `@expo/vector-icons` (Ionicons)
- **Platform Support**: Android, iOS, Web

## Getting Started

### Prerequisites

- Node.js (v18 or newer)
- npm or yarn
- Expo Go app on mobile (optional, for device testing)

### Installation

1. Clone this repository:
   ```bash
   git clone <REPOSITORY_URL>
   cd profiledetailsapp
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

### Running the App

Start the Expo development server:

```bash
npx expo start
```

- Press `w` to open in your web browser.
- Press `a` to run on Android emulator / connected device.
- Press `i` to run on iOS simulator (macOS required).
- Scan the displayed QR code with the Expo Go app on your physical mobile device.
