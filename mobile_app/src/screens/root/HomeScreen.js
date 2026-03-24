import React, { useState } from "react";
import {
  Alert,
  Linking,
  RefreshControl,
  ScrollView,
  StyleSheet,
  TouchableOpacity,
  View,
} from "react-native";

import { SPACINGS } from "../../core/theme";
import { ROUTES } from "../../core/constants/routes";

import Profile from "../../components/home/Profile";
import DashboardTile from "../../components/home/DashboardTile";
import { IMAGES } from "../../core/constants/images";
import { useDispatch, useSelector } from "react-redux";
import { getBuildingWmslink } from "../../service/building_service";
import {
  emptyingService,
  getLanguagesList,
} from "../../service/supervisor_service";
import { useEffect } from "react";
import LoadingSpinner from "../../components/common/LoadingSpinner";
import { Header } from "../../components/headers";
import { Text, useTheme } from "react-native-paper";
import colors from "../../core/theme/colors";
import { setLanguages } from "../../store/slices/auth.slice";
import {
  BRANDING,
  getPrimaryBrandUrl,
} from "../../core/constants/branding";

const HomeScreen = ({ navigation }) => {
  const { contentsLabel } = useSelector((state) => state.auth);
  const getLabel = (key) => contentsLabel?.[key] || key;
  const navigateTo = (screen, params) => {
    navigation.navigate(screen, params);
  };

  const dispatch = useDispatch();
  const [loading, setLoading] = useState(false);

  const { permissions } = useSelector((state) => state.auth);

  useEffect(() => {
    getPermissions();
  }, []);

  const getPermissions = () => {
    setLoading(true);
    fetchLanguages();
    if (permissions["building-survey"] === true) {
      console.log("surveyer");
      getBuildingWmslink()
        .then((response) => {
          console.log("logged in");
        })
        .catch((err) => {
          setLoading(false);
          return;
        });
    }

    if (permissions["save-assessment"] === true) {
      emptyingService()
        .then((response) => {
          console.log("logged in");
        })
        .catch((err) => {
          setLoading(false);
          console.log("Error!!", err);
          return;
        });
    }

    if (permissions["save-emptying-service"] === true) {
      console.log("supervisor");
      emptyingService()
        .then((response) => {
          console.log("logged in");
        })
        .catch((err) => {
          setLoading(false);
          console.log("Error!!", err);
          return;
        });
    }

    setTimeout(() => {
      setLoading(false);
    }, 5000);
  };
  const fetchLanguages = async () => {
    try {
      getLanguagesList()
        .then((response) => {
          if (response?.data?.languages) {
            dispatch(setLanguages(response?.data?.languages));
          }
        })
        .catch((err) => {
          console.log("Error!!", err);
          return;
        });
    } catch (error) {
      console.error("Failed to fetch languages:", error);
    }
  };
  const openExternalLink = async (url) => {
    if (!url) {
      Alert.alert(
        "Lien non configure",
        "Renseignez les variables de branding pour publier vos liens."
      );
      return;
    }

    try {
      await Linking.openURL(url);
    } catch (error) {
      Alert.alert("Ouverture impossible", "Le lien n'a pas pu etre ouvert.");
    }
  };

  const openPrimaryBrandLink = () => {
    openExternalLink(getPrimaryBrandUrl());
  };

  const openPublicGithub = () => {
    openExternalLink(BRANDING.githubUrl);
  };

  const openPublicYoutube = () => {
    openExternalLink(BRANDING.youtubeUrl);
  };

  const openOriginalRepository = () => {
    openExternalLink(BRANDING.originalRepositoryUrl);
  };

  const openCCLicense = () => {
    openExternalLink(BRANDING.originalLicenseUrl);
  };
  const theme = useTheme();

  return (
    <View style={[styles.container]}>
      <Header title={getLabel("Home")} type="home" hideBackAction={true} />
      <ScrollView
        contentContainerStyle={{ flexGrow: 1 }}
        showsVerticalScrollIndicator={false}
        refreshControl={
          <RefreshControl onRefresh={getPermissions} refreshing={false} />
        }
      >
        <Profile />
        <LoadingSpinner isVisible={loading} title={"Loading"} />
        <View
          style={{
            flex: 1,
            backgroundColor: theme.colors.elevation.level1,
            borderTopLeftRadius: 12,
            borderTopRightRadius: 12,
            marginTop: -12,
          }}
        >
          <View style={[styles.dbContainer]}>
            {permissions["building-survey"] && (
              <>
                <DashboardTile
                  title={getLabel("Building Map")}
                  image={IMAGES.buildings}
                  onPress={() => navigateTo(ROUTES.building_map, {})}
                />

                {/* <DashboardTile
              title={'Containment Map'}
              image={IMAGES.containment}
              onPress={() => navigateTo(ROUTES.containment_map, {})}
            /> */}

                <DashboardTile
                  title={getLabel("Buildings Data")}
                  image={IMAGES.buildings_data}
                  onPress={() => navigateTo(ROUTES.building_data, {})}
                />

                {/* <DashboardTile
              title={'Containments Data'}
              image={IMAGES.containment_data}
              onPress={() => navigateTo(ROUTES.containment_data, {})}
            /> */}
              </>
            )}
            {/* {permissions['save-assessment'] && (
            <DashboardTile
              title={'Containment Assessment'}
              image={IMAGES.assessment}
              onPress={() =>
                navigateTo(ROUTES.application_list, {assessment: true})
              }
            />
          )} */}
            {permissions["save-emptying-service"] && (
              <DashboardTile
                title={getLabel("Emptying Service")}
                image={IMAGES.emptying}
                onPress={() =>
                  navigateTo(ROUTES.application_list, { emptying: true })
                }
              />
            )}
            {permissions["sewer-connection"] && (
              <DashboardTile
                title={getLabel("Sewer Map")}
                image={IMAGES.emptying}
                onPress={() => navigateTo(ROUTES.sewage_map)}
              />
            )}
            {permissions["sewer-connection"] && (
              <DashboardTile
                title={getLabel("Sewer Data")}
                image={IMAGES.assessment}
                onPress={() => navigateTo(ROUTES.sewage_data)}
              />
            )}
            {/* <DashboardTile
          title={'Land'}
          onPress={() => navigateTo(ROUTES.land_service)}
          image={IMAGES.land}
        /> */}
          </View>
          <View style={[styles.bottomContainer]}>
            <Text style={styles.bottomText} variant="labelLarge">
              Personnalisation Mali :{" "}
              <Text
                style={styles.bottomLink}
                variant="labelLarge"
                onPress={openPrimaryBrandLink}
              >
                {BRANDING.organizationName}
              </Text>
              .{"\n"}
              Base sur{" "}
              <Text
                style={styles.bottomLink}
                variant="labelLarge"
                onPress={openOriginalRepository}
              >
                {BRANDING.originalProjectName}
              </Text>{" "}
              . Credits originaux : {BRANDING.originalCreators}. Licence{" "}
              <Text
                variant="labelLarge"
                style={styles.bottomLink}
                onPress={openCCLicense}
              >
                {BRANDING.originalLicenseName}
              </Text>
              .
            </Text>
            <View style={styles.publicLinks}>
              {BRANDING.githubUrl ? (
                <TouchableOpacity onPress={openPublicGithub} style={styles.publicLinkAction}>
                  <Text style={styles.bottomLink} variant="labelLarge">
                    GitHub
                  </Text>
                </TouchableOpacity>
              ) : null}
              {BRANDING.youtubeUrl ? (
                <TouchableOpacity onPress={openPublicYoutube} style={styles.publicLinkAction}>
                  <Text style={styles.bottomLink} variant="labelLarge">
                    YouTube
                  </Text>
                </TouchableOpacity>
              ) : null}
            </View>
          </View>
        </View>
      </ScrollView>
    </View>
  );
};

export default HomeScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  bottomContainer: {
    flex: 1,
    justifyContent: "flex-end",
    padding: 12,
    marginTop: 18,
  },
  bottomText: {
    textAlign: "center",
    color: colors.darkGrey,
  },
  publicLinks: {
    alignItems: "center",
    flexDirection: "row",
    justifyContent: "center",
    marginTop: 8,
  },
  publicLinkAction: {
    marginHorizontal: 8,
  },
  bottomLink: {
    color: "rgb(30, 77, 120)",
    lineHeight: 20,
  },
  dbContainer: {
    flex: 1,
    padding: SPACINGS.sm,
    flexWrap: "wrap",
    flexDirection: "row",
    justifyContent: "center",
  },
});
