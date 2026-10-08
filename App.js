import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableOpacity,
  SafeAreaView,
  StatusBar,
  Platform,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

export default function App() {
  const [points, setPoints] = useState(0);

  const handleAddPoint = () => {
    setPoints((prevPoints) => prevPoints + 1);
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="light-content" backgroundColor="#000000" />
      
      <View style={styles.rootWrapper}>
        <View style={styles.container}>
          {/* Top App Bar / Header */}
          <View style={styles.header}>
            <Text style={styles.headerTitle}>My Profile</Text>
          </View>

          {/* Profile Avatar Section */}
        <View style={styles.avatarSection}>
          <View style={styles.avatarContainer}>
            <Image
              source={require('./assets/avatar.png')}
              style={styles.avatarImage}
              resizeMode="contain"
            />
          </View>
        </View>

        {/* Divider Line */}
        <View style={styles.divider} />

        {/* User Information Section */}
        <View style={styles.infoSection}>
          {/* Name Field */}
          <View style={styles.infoGroup}>
            <Text style={styles.label}>Name</Text>
            <Text style={styles.value}>Diluka</Text>
          </View>

          {/* Email Field */}
          <View style={styles.infoGroup}>
            <Text style={styles.label}>Email</Text>
            <View style={styles.iconValueRow}>
              <Ionicons name="mail" size={20} color="#111111" style={styles.fieldIcon} />
              <Text style={styles.value}>diluka.w@nsbm.ac.lk</Text>
            </View>
          </View>

          {/* Points Field */}
          <View style={styles.infoGroup}>
            <Text style={styles.label}>Points</Text>
            <View style={styles.iconValueRow}>
              <Ionicons name="star" size={20} color="#111111" style={styles.fieldIcon} />
              <Text style={styles.value}>{points}</Text>
            </View>
          </View>
        </View>

        {/* Floating Action Button (FAB) */}
        <TouchableOpacity
          style={styles.fab}
          onPress={handleAddPoint}
          activeOpacity={0.8}
          accessibilityLabel="Add Point"
          accessibilityRole="button"
        >
          <Ionicons name="add" size={28} color="#FFFFFF" />
        </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#000000',
    paddingTop: Platform.OS === 'android' ? StatusBar.currentHeight : 0,
  },
  rootWrapper: {
    flex: 1,
    backgroundColor: Platform.OS === 'web' ? '#E9ECEF' : '#F5F5F5',
    justifyContent: 'center',
    alignItems: 'center',
  },
  header: {
    height: 58,
    backgroundColor: '#000000',
    justifyContent: 'center',
    alignItems: 'center',
    width: '100%',
  },
  headerTitle: {
    color: '#FFFFFF',
    fontSize: 20,
    fontWeight: '700',
    letterSpacing: 0.3,
  },
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
    width: '100%',
    maxWidth: 440,
    position: 'relative',
    ...(Platform.OS === 'web'
      ? {
          shadowColor: '#000',
          shadowOffset: { width: 0, height: 6 },
          shadowOpacity: 0.15,
          shadowRadius: 16,
        }
      : {}),
  },
  avatarSection: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: 36,
    paddingBottom: 28,
  },
  avatarContainer: {
    width: 140,
    height: 140,
    borderRadius: 70,
    backgroundColor: '#FFFFFF',
    justifyContent: 'center',
    alignItems: 'center',
    // subtle border / shadow
    borderWidth: 1,
    borderColor: '#E6E6E6',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.08,
    shadowRadius: 4,
    elevation: 2,
    overflow: 'hidden',
  },
  avatarImage: {
    width: 136,
    height: 136,
  },
  divider: {
    height: 1.5,
    backgroundColor: '#1E1E1E',
    marginHorizontal: 26,
    marginBottom: 24,
  },
  infoSection: {
    paddingHorizontal: 26,
  },
  infoGroup: {
    marginBottom: 24,
  },
  label: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#000000',
    marginBottom: 8,
  },
  value: {
    fontSize: 17,
    color: '#555555',
    fontWeight: '400',
  },
  iconValueRow: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  fieldIcon: {
    marginRight: 10,
  },
  fab: {
    position: 'absolute',
    right: 28,
    bottom: 32,
    width: 58,
    height: 58,
    borderRadius: 29,
    backgroundColor: '#000000',
    justifyContent: 'center',
    alignItems: 'center',
    // Shadow for iOS and Android
    elevation: 6,
    shadowColor: '#000000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.35,
    shadowRadius: 5,
  },
});
