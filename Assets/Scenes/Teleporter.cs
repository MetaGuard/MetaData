using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Teleporter : MonoBehaviour {
    int index = 1;
    int b = 0;
    int u = 0;
    int m = 0;
    public GameObject b1;
    public GameObject b2;
    public GameObject b3;
    public AudioSource bs;
    public AudioClip win;
    public AudioClip pop;
    public GameObject c1;
    public GameObject c2;
    public GameObject c3;
    public GameObject c4;
    public GameObject m1;
    public GameObject m2;
    public GameObject m3;
    public GameObject m4;
    public GameObject m5;
    public GameObject m6;
    public GameObject m7;
    public GameObject m8;
    public GameObject m9;
    public GameObject m10;

    void Start() {
      this.transform.position = new Vector3(-7.698f, -3.5f, -17.471f);  // room 1 - hello
    }

    void Update() {
      Vector3[] pos = new Vector3[] {
        new Vector3(-7.698f, -3.5f, -17.471f),  // room 1 - hello
        new Vector3(-7.698f, -3.5f, -12.471f),  // room 2 - face
        new Vector3(-7.698f, -3.5f, -2.044f),   // room 3 - captcha - velvet
        new Vector3(-10.701f, 0f, -4.24f),      // room 4 - find letters - church
        new Vector3(10.391f, 0f, -4.24f),       // room 5 - color vision - daisy
        new Vector3(25.165f, 0f, -9.365f),      // room 6 - proximity - red
        new Vector3(15.658f, 0f, -15.61f),      // room 7 - MOCA - recluse
        new Vector3(-25.475f, 0f, -7.88f),      // room 8 - wingspan - cave
        new Vector3(-15.587f, 0f, -17.425f),    // room 9 - fitness - motivation
        new Vector3(-21.032f, 0f, -16.16f),     // room 10 - puzzle - deafening
        new Vector3(21.01f, 0f, -15.04f),       // room 11 - reaction time - flash
        new Vector3(-22.149f, 3.5f, -17.242f),  // room 12 - ceiling - flash
        new Vector3(-22.149f, 3.5f, -17.242f),  // room 13 - language - apple
        new Vector3(-25.293f, 3.5f, -8.354f)    // room 14 - pattern - i can
      };

      if (Input.GetKeyDown("space")) {
        this.transform.position = pos[index++];
        bs.PlayOneShot(win, 1f);
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
        u = 0;
        m = 0;
        b1.SetActive(true);
        b2.SetActive(true);
        b3.SetActive(true);
        c1.SetActive(true);
        c2.SetActive(true);
        c3.SetActive(true);
        c4.SetActive(true);
        m1.SetActive(true);
        m2.SetActive(true);
        m3.SetActive(true);
        m4.SetActive(true);
        m5.SetActive(true);
        m6.SetActive(true);
        m7.SetActive(true);
        m8.SetActive(true);
        m9.SetActive(true);
        m10.SetActive(true);
      }

      if (Input.GetKeyDown("u")) {
        u++;
        if (u == 1) c1.SetActive(false);
        if (u == 2) c2.SetActive(false);
        if (u == 3) c3.SetActive(false);
        if (u == 4) c4.SetActive(false);
      }

      if (Input.GetKeyDown("m")) {
        m++;
        if (m == 1) m1.SetActive(false);
        if (m == 2) m2.SetActive(false);
        if (m == 3) m3.SetActive(false);
        if (m == 4) m4.SetActive(false);
        if (m == 5) m5.SetActive(false);
        if (m == 6) m6.SetActive(false);
        if (m == 7) m7.SetActive(false);
        if (m == 8) m8.SetActive(false);
        if (m == 9) m9.SetActive(false);
        if (m == 10) m10.SetActive(false);
      }
    }
}
