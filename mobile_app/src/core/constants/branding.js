import Config from "react-native-config";

const normalize = (value) => {
  if (typeof value !== "string") {
    return "";
  }

  return value.trim();
};

export const BRANDING = {
  appName: normalize(Config.BRAND_APP_NAME) || "Systeme de gestion municipale - Mali",
  shortName: normalize(Config.BRAND_SHORT_NAME) || "SGM Mali",
  organizationName: normalize(Config.BRAND_ORGANIZATION_NAME) || "Mairie du Mali",
  contactEmail: normalize(Config.BRAND_CONTACT_EMAIL) || "contact@mairie.local",
  websiteUrl: normalize(Config.BRAND_PUBLIC_WEBSITE_URL),
  githubUrl: normalize(Config.BRAND_PUBLIC_GITHUB_URL),
  youtubeUrl: normalize(Config.BRAND_PUBLIC_YOUTUBE_URL),
  originalProjectName: "Base IMIS",
  originalRepositoryUrl: "https://github.com/base-imis/.github",
  originalLicenseName: "CC BY-NC-SA 4.0",
  originalLicenseUrl: "https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1",
  originalCreators: "Innovative Solution Pvt. Ltd. (ISPL) et GWSC-AIT",
};

export const getPrimaryBrandUrl = () =>
  BRANDING.websiteUrl || BRANDING.githubUrl || BRANDING.youtubeUrl || "";
