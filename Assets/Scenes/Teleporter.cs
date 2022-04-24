using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Teleporter : MonoBehaviour {
    int index = 1;
    int b = 0;
    public GameObject b1;
    public GameObject b2;
    public GameObject b3;
    public AudioSource bs;
    public AudioClip pop;

    void Start() {
      this.transform.position = new Vector3(-7.698f, -3.5f, -17.471f);  // room 1 - hello
    }

    void Update() {
      Vector3[] pos = new Vector3[] {
        new Vector3(-7.698f, -3.5f, -17.471f),  // room 1 - hello
        new Vector3(-7.698f, -3.5f, -12.471f),  // room 2 - face
        new Vector3(-7.698f, -3.5f, -3.044f),   // room 3 - captcha - velvet
        new Vector3(-10.701f, 0f, -4.24f),   // room 4 - find letters - church
        new Vector3(10.391f, 0f, -4.24f),   // room 5 - color vision - daisy
        new Vector3(25.165f, 0f, -9.365f)   // room 6 - proximity - red
      };

      if (Input.GetKeyDown("space")) {
        this.transform.position = pos[index++];
      }

      if (Input.GetKeyDown("b")) {
        this.transform.position = pos[--index];
      }

      if (Input.GetKeyDown("p")) {
        b++;
        if (b == 1) b1.SetActive(false);
        if (b == 2) b2.SetActive(false);
        if (b == 3) b3.SetActive(false);
        bs.PlayOneShot(pop, 1f);
      }

      if (Input.GetKeyDown("r")) {
        b = 0;
        b1.SetActive(true);
        b2.SetActive(true);
        b3.SetActive(true);
      }
    }
}
